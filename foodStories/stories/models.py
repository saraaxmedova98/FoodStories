from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Story(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    story_image = models.FileField(_("Story file"), upload_to="story_images", max_length=100, blank=True, null=True)

    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE, null=True)
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True)

    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True, null = True)


    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
    
    def __str__(self):
        return self.title
    

class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    ingredients = models.TextField(_("Ingredients"))
    directions = models.TextField(_("Directions"), default="")
    prepare_time = models.CharField(_("Prepare time"), max_length=50)
    recipe_image = models.ImageField(_("Image"), upload_to='recipe_images', blank=True, null=True)

    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True)
    authors = models.ManyToManyField("stories.Author", verbose_name=_("Authors"))
    
    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title
    
class Author(models.Model):
    first_name = models.CharField(_("Name"), max_length=50)
    last_name = models.CharField(_("Surname"), max_length=50)
    username = models.CharField(_("Username"), max_length=50 , blank=True)
    email = models.EmailField(_("Email"), max_length=254, null=True)
    bio = models.TextField(_("Biography"), blank=True, null=True)
    password = models.CharField(_("Password"), max_length=50, null=True)
    image = models.ImageField(_("Image"), upload_to='partials', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.first_name
    
class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50, default="")
    image = models.ImageField(_("Image"), upload_to='partials', blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    title = models.CharField(_("Title"), max_length=50, blank=True, null=True)

    stories = models.ManyToManyField("stories.Story", verbose_name=_("Story"))
    recipes = models.ManyToManyField("stories.Recipe", verbose_name=_("Recipe"))
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    message = models.TextField(_("Description"))
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)
    
    comment_reply = models.ForeignKey("self", verbose_name=_("Comment"), on_delete=models.CASCADE, blank=True, null = True)
    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE, blank=True, null=True)
    recipe = models.ForeignKey("stories.Recipe", verbose_name=_("Recipe"), on_delete=models.CASCADE)
    story = models.ForeignKey("stories.Story", verbose_name=_("Story"), on_delete=models.CASCADE, blank=True, null=True)
    
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


class FooterInfo(models.Model):
    location = models.CharField(_("Location"), max_length=50)
    phone = models.CharField(_("Phone number"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    facebook = models.URLField(_("Facebook"), max_length=200, blank=True, null=True)
    twitter = models.URLField(_("Twitter"), max_length=200, blank=True, null=True)
    instagram = models.URLField(_("Instagram"), max_length=200, blank=True, null=True)
    

    class Meta:
        verbose_name = _("FooterInfo")
        verbose_name_plural = _("FooterInfos")

    def __str__(self):
        return self.email

  