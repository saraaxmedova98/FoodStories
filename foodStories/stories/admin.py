from django.contrib import admin
from stories.models import Contact, Recipe, Comment, Story , Category,Subscribe, SiteSettings,\
     SumNumbers, StoryImage


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
class StoryAdmin(admin.ModelAdmin):
    inlines = [StoryImageAdmin]
    list_display = ['title', 'description', 'story_image', 'category','updated_at','created_at']
    ordering = ['created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'category']
    fieldsets = (
        ('Required Fields', {
            "fields": ('title','description','tags'),
        }),
        ('Optional Fields', {
            "fields": ('story_image', 'cover_image',),
            'classes': ('collapse',),

        }),
        ('Relational Fields', {
            "fields": ('category','user'),
            'classes': ('collapse',),
        }),

    )

@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ['images']
    


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'ingredients', 'prepare_time','recipe_image', 'category']
    ordering = ['title']
    search_fields = ['title', 'description']
    list_filter = ['created_at','category']
    fieldsets = (
        ('Required Fields', {
            "fields": ('title','ingredients','prepare_time',),
        }),
        ('Optional Fields', {
            "fields": ('description','recipe_image','cover_image',),
            'classes': ('collapse',),

        }),
        ('Relational Fields', {
            "fields": ('category','user'),
            'classes': ('collapse',),
        }),

    )
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['message', 'recipe', 'story']
    ordering = ['message']
    search_fields = ['message']
    list_filter = ['commented_at', 'recipe', 'story']
    fieldsets = (
        ('Required Fields', {
            "fields": ('message',),
        }),
        ('Relational Fields', {
            "fields": ('comment_reply','recipe', 'story',),
            'classes': ('collapse',),
        }),

    )

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     ordering = ['title']
#     search_fields = ['title']
#     list_filter = ['stories', 'recipes']
#     fieldsets = (
#         ('Required Fields', {
#             "fields": ('title',),
#         }),
#         ('Relational Fields', {
#             "fields": ('stories','recipes',),
#             'classes': ('collapse',),
#         }),

#     )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    ordering = ['title']
    search_fields = ['title']
    list_filter = ['title']

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

    # MAX_OBJECTS = 1

    # def has_add_permission(self, request):
    #     if self.model.objects.count() >= MAX_OBJECTS:
    #         return False
    #     return super().has_add_permission(request)
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
    

@admin.register(SumNumbers)
class SUmNumbersAdmin(admin.ModelAdmin):
    list_display= ['sum']
    

    

    




    

    
    

