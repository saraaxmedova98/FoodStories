from django.contrib import admin
from stories.models import Author,Contact, Recipe, Comment, Story , Tag, Category, Subscribe, FooterInfo


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
# def change_user( modeladmin, request, queryset):
#         queryset.update(username = 'user')
# change_user.short_description = 'change username'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'username', 'email']
    ordering=['first_name']
    search_fields = ['first_name', 'username']
    list_filter = ['username']
    actions = ['change_user']
    fieldsets = (
        ('Required Fields', {
            "fields": ('first_name','last_name', 'email', 'password'),
        }),
        ('Optional Fields', {
            "fields": ('username','bio','image',),
            'classes': ('collapse',),
        }),
    
    )

    def change_user( self, request, queryset):
        queryset.update(username = 'user')
    change_user.short_description = 'change username'

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'story_image', 'author', 'category']
    ordering = ['title']
    search_fields = ['title']
    list_filter = ['created_at','author', 'category']
    fieldsets = (
        ('Required Fields', {
            "fields": ('title',),
        }),
        ('Optional Fields', {
            "fields": ('description','story_image',),
            'classes': ('collapse',),

        }),
        ('Relational Fields', {
            "fields": ('category','author',),
            'classes': ('collapse',),
        }),

    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'ingredients', 'directions', 'prepare_time','recipe_image', 'category']
    ordering = ['title']
    search_fields = ['title', 'description']
    list_filter = ['created_at','category']
    fieldsets = (
        ('Required Fields', {
            "fields": ('title','ingredients','prepare_time',),
        }),
        ('Optional Fields', {
            "fields": ('description','directions','recipe_image',),
            'classes': ('collapse',),

        }),
        ('Relational Fields', {
            "fields": ('category','authors',),
            'classes': ('collapse',),
        }),

    )
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['message', 'author', 'recipe', 'story']
    ordering = ['message']
    search_fields = ['message']
    list_filter = ['commented_at','author', 'recipe', 'story']
    fieldsets = (
        ('Required Fields', {
            "fields": ('message',),
        }),
        ('Relational Fields', {
            "fields": ('comment_reply','author','recipe', 'story',),
            'classes': ('collapse',),
        }),

    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    search_fields = ['title']
    list_filter = ['stories', 'recipes']
    fieldsets = (
        ('Required Fields', {
            "fields": ('title',),
        }),
        ('Relational Fields', {
            "fields": ('stories','recipes',),
            'classes': ('collapse',),
        }),

    )

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
    

@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ['location', 'phone', 'email', 'facebook', 'twitter', 'instagram']
    ordering = ['email']
    search_fields = ['email', 'location']

    


    

    

    




    

    
    

