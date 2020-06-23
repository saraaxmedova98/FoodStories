from django.db import models
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Story(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    story_image = models.FileField(_("Story file"), upload_to="stories", max_length=100, blank=True, null=True)
    cover_image = models.FileField(_("Cover image"), upload_to="stories",  max_length=None, default="bg_4.jpg")
    story_count = models.IntegerField(_("Story count"), default=0)
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)
    tags = TaggableManager()
    
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True, related_name='stories')
    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True, null = True)
    user = models.ForeignKey("account.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE, null=True)
   

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('stories:story_detail', kwargs={'pk': self.pk})


class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    ingredients = models.TextField(_("Ingredients"))
    directions = models.TextField(_("Directions"), default="")
    prepare_time = models.CharField(_("Prepare time"), max_length=50)
    recipe_image = models.ImageField(_("Recipe Image"), upload_to='recipes/', blank=True, null=True)
    cover_image = models.ImageField(_("Cover image"), upload_to='stories', default='bg_4.jpg')
    recipe_count = models.IntegerField(_("Recipe count"), default=0)
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True, related_name='recipes')                                                                       
    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True)
    users = models.ManyToManyField("account.CustomUser", verbose_name=_("User"), related_name='recipes', null=True)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stories:recipe_detail', kwargs={'pk': self.pk})
    

    
class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50, default="")
    image = models.ImageField(_("Image"), upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    
    
    
class Tag(models.Model):
    title = models.CharField(_("Title"), max_length=50, blank=True, null=True)

    stories = models.ManyToManyField("stories.Story", verbose_name=_("Story"), related_name='stories')
    recipes = models.ManyToManyField("stories.Recipe", verbose_name=_("Recipe"), related_name='recipes')
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(_("Name"), max_length=50, default='user')
    email = models.EmailField(_("Email"), max_length=254, default='user@gmail.com')
    message = models.TextField(_("Description"))
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)
    
    comment_reply = models.ForeignKey("self", verbose_name=_("Comment"), on_delete=models.CASCADE, blank=True, null = True)
    recipe = models.ForeignKey("stories.Recipe", verbose_name=_("Recipe"), on_delete=models.CASCADE, blank=True, null=True)
    story = models.ForeignKey("stories.Story", verbose_name=_("Story"), on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey("account.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE, blank=True, null=True)
   
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.message

class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50, blank=True, null=True)
    message = models.TextField(_("Message"))
    source = models.CharField(_("Source"), max_length=50, blank=True, null=True)
    contacted_at = models.DateField(_("Contacted at"), auto_now_add=True, blank= True, null=True)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
    

class Subscribe(models.Model):
    email = models.EmailField(_("Email"), max_length=254)

    subscribed_at = models.DateField(_("Subscribed at"), auto_now_add=True, blank= True, null=True)

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'
    
    def __str__(self):
        return self.email


class SiteSettings(models.Model):
    address = models.CharField(_("Location"), max_length=50)
    phone = models.CharField(_("Phone number"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    website = models.URLField(_("Website"), max_length=200)
    facebook = models.URLField(_("Facebook"), max_length=200, blank=True, null=True)
    twitter = models.URLField(_("Twitter"), max_length=200, blank=True, null=True)
    instagram = models.URLField(_("Instagram"), max_length=200, blank=True, null=True)
    


    def __str__(self):
        return self.email

  