from django.db import models
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class TaggedStory(TaggedItemBase):
    content_object = models.ForeignKey('Story', on_delete=models.CASCADE, related_name='story', blank=True, null=True)
   

class Story(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    story_image = models.ImageField(_("Story image"),upload_to='stories/', blank=True, null=True)
    cover_image = models.ImageField(_("Cover image"), upload_to="stories/",  max_length=None, blank=True, null=True)
    story_count = models.IntegerField(_("Story count"), default=0)
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)
    tags = TaggableManager(through=TaggedStory, blank=True)
    
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True, related_name='stories')
    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True, null = True)
    user = models.ForeignKey("account.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE, null=True, related_name='story')
   

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('stories:story_detail', kwargs={'pk': self.pk})

    def comment_count(self,):
        return self.comment.all().count()


class StoryImage(models.Model):
    images = models.ImageField(_("Story image"), upload_to='stories/')
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE,blank=True, null=True, related_name='images')

    class Meta:
        verbose_name = _("Story Image")
        verbose_name_plural = _("Story Images")

    def __str__(self):
        return self.story.title


class TaggedRecipe(TaggedItemBase):
    content_object = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipe')


class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    ingredients = models.TextField(_("Ingredients"))
    prepare_time = models.CharField(_("Prepare time"), max_length=50, blank=True, null=True)
    recipe_image = models.ImageField(_("Recipe Image"), upload_to='recipes/', blank=True, null=True)
    cover_image = models.ImageField(_("Cover image"), upload_to='recipes/', blank=True, null=True)
    recipe_count = models.IntegerField(_("Recipe count"), default=0)
    tags = TaggableManager(through=TaggedRecipe, blank=True)

    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True)
    user = models.ForeignKey("account.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE, null=True, related_name='user')
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True, related_name='recipes')                                                                       
    
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
    
 
class Comment(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    message = models.TextField(_("Description"))
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)
    active = models.BooleanField(default=False)

    comment_reply = models.ForeignKey("self", verbose_name=_("Comment"), on_delete=models.CASCADE, blank=True, null = True, related_name='replies')
    recipe = models.ForeignKey("stories.Recipe", verbose_name=_("Recipe"), on_delete=models.CASCADE, blank=True, null=True, related_name='comment')
    story = models.ForeignKey("stories.Story", verbose_name=_("Story"), on_delete=models.CASCADE, blank=True, null=True, related_name='comment')
    user = models.ForeignKey("account.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE, blank=True, null=True, related_name='comment')
   
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

  
class SumNumbers(models.Model):
    sum = models.IntegerField(_("Sum"))
    


    def __str__(self):
        return str(self.sum)

