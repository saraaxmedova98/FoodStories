from django.contrib import admin
from stories.models import *
from django.db.models import Count
import csv
from django.http import HttpResponse
from django.utils.safestring import mark_safe

class ExportCsvMixin(object):
    csv_fields = None
    csv_urlname = None
    csv_filename = 'export'

    def __init__(self, *args, **kwargs):
        if not self.csv_fields or not self.csv_urlname:
            raise ValueError(_(u'A list of fields for the csv and an urlname for this action must be defined.'))
        
        super(ExportCsvMixin, self).__init__(*args, **kwargs)

    def _get_model_field(self, name, model=None):
        """
        Obtain the field of a model based on its name
        name -- name of the field
        model -- model on where to get the field
        """
        if not model:
            model = self.model

        try:
            value = model._meta.get_field(name).verbose_name
            if not isinstance(value, str) and not isinstance(value, unicode):
                value = value._proxy____unicode_cast()
        except FieldDoesNotExist:
            value = '-'

        return value

    def _get_instance_value(self, instance, attr):
        """
        Get the value of an attribute of the instance
        instance -- an instance of the model
        attr -- the attribute to which retrieve a value
        """
        value = getattr(instance, attr)

        if callable(value):
            value = value()
        
        if not value:
            value = '-'
        
        return u'%s' % value

    def _get_instance_values(self, instance, attrs):
        """
        Get the values of a attributes list of the instance
        instance -- an instance of the model
        attrs -- a list of attributes for which to obtain values
        """
        return [self._get_instance_value(instance, attr) for attr in attrs]

    def export_csv(self, request):
        """
        Create a csv file and return it as a HttResponse
        request -- a HttpResponse
        """
        objs = self.model.objects.all().select_related()

        rows = []
        for obj in objs:
            row = []
            row.extend(self._get_instance_values(obj, self.csv_fields))

            rows.append(','.join(row))

        row = []
        [row.append(self._get_model_field(attr)) for attr in self.csv_fields]
        rows.insert(0, ','.join(row))

        csv = '\r\n'.join(rows)
        csv = csv.encode('iso-8859-1')

        response = HttpResponse(csv, mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % self.csv_filename

        return response

    def get_urls(self):
        """
        Override the get_urls method from ModelAdmin adding the export_subscriptions url
        """
        original_urls = super(ExportCsvMixin, self).get_urls()
        new_urls = patterns('',
            url(r'export/$', self.admin_site.admin_view(self.export_csv), name=self.csv_urlname)
        )

        return new_urls + original_urls
    
    def changelist_view(self, request, extra_context=None):
        """
        Pass the url for export this csv on the extra_context parameter for the changelist
        """
        if extra_context:
            extra_context.update({ 'export_url': reverse('admin:%s' % self.csv_urlname) })
        else:
            extra_context = { 'export_url': reverse('admin:%s' % self.csv_urlname) }

        return super(ExportCsvMixin, self).changelist_view(request, extra_context)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display= ['name', 'email','subject', 'message']
    ordering=('name',)
    search_fields=('name', 'email')
    list_filter=('contacted_at',)
    fieldsets = (
        (
            'Required Fields', {
                'description': 'These fields are required',
                'fields' : ['name', 'email','message']
        }),
        (
            'Optional Fields' , {
                'description': 'These fields are optional',
                'classes': ['collapse'],
                'fields' : ['subject',]
        }),
    )

    def change_user( self, request, queryset):
        queryset.update(username = 'user')
    change_user.short_description = 'change username'


class StoryImageAdmin(admin.StackedInline):
    model = StoryImage


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    inlines = [StoryImageAdmin]
    list_display = ['title', 'description', 'category', 'comment_count','updated_at','created_at']
    ordering = ['created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'category']
    list_per_page = 6
    readonly_fields = ["image_story", 'story_cover_image', 'updated_at', 'created_at']
    date_hierarchy = 'created_at'
    raw_id_fields = ["category"]

    fieldsets = (
        ('Required Fields', {
            "fields": ('title','description','tags'),
        }),
        ('Optional Fields', {
            "fields": ('story_image','image_story', 'cover_image', 'story_cover_image','updated_at', 'created_at'),
            'classes': ('collapse',),

        }),
        ('Relational Fields', {
            "fields": ('category','user',),
            'classes': ('collapse',),
        }),

    )


    def image_story(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} style="object-fit: cover;" />'.format(
            url = obj.story_image.url,
            width='200px',
            height='200px',
            )
    )

    def story_cover_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} style="object-fit: cover;" />'.format(
            url = obj.cover_image.url,
            width='200px',
            height='200px',
            )
    )

  
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "category":
    #         kwargs["queryset"] = Category.objects.filter(title__in=['Beans', 'Main Dish'])
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ['images']
    

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'comment_count', 'category','updated_at', 'created_at']
    ordering = ['title']
    search_fields = ['title', 'description']
    list_filter = ['created_at','category']
    readonly_fields = ["image_recipe", 'recipe_cover_image' , 'updated_at', 'created_at']
    fieldsets = (
        ('Required Fields', {
            "fields": ('title','ingredients','prepare_time','tags',),
        }),
        ('Optional Fields', {
            "fields": ('description','recipe_image','image_recipe','cover_image', 'recipe_cover_image' ,'updated_at', 'created_at' ),
            'classes': ('collapse',),

        }),
        ('Relational Fields', {
            "fields": ('category','user'),
            'classes': ('collapse',),
        }),

    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _comment_count=Count("comment", distinct=True),
            
        )
        return queryset

    def comment_count(self, obj):
        return obj._comment_count

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        queryset.update(ingredients = 'salt, sugar, icecream')

    export_as_csv.short_description = "Add ingredients"


    def image_recipe(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} style="object-fit: cover;" />'.format(
            url = obj.recipe_image.url,
            width='200px',
            height='200px',
            )
    )

    def recipe_cover_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} style="object-fit: cover;" />'.format(
            url = obj.cover_image.url,
            width='200px',
            height='200px',
            )
    )

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'message','active', 'recipe', 'story']
    ordering = ['message']
    search_fields = ['message']
    list_filter = ['commented_at', 'recipe', 'story']
    fieldsets = (
        ('Required Fields', {
            "fields": ('name','email','message', 'active',),
        }),
        ('Relational Fields', {
            "fields": ('comment_reply','recipe', 'story',),
            'classes': ('collapse',),
        }),

    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','story_display']
    ordering = ['title']
    search_fields = ['title']
    list_filter = ['title']

    def has_delete_permission(self, request, obj=None):
        return False

    def story_display(self, obj):
        return ", ".join([
            story.title for story in obj.stories.all()
        ])
    story_display.short_description = "Stories"

    readonly_fields = ["category_image"]

    def category_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} style="object-fit: cover;" />'.format(
            url = obj.image.url,
            width='200px',
            height='200px',
            )
    )
    

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']
    ordering = ['email']
    search_fields = ['email']
    list_filter = ['subscribed_at']
    

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email','website', 'facebook', 'twitter', 'instagram']
    ordering = ['email']
    search_fields = ['email', 'location']



    def has_add_permission(self, request):
        MAX_OBJECTS = 1
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
    

    

    




    

    
    

