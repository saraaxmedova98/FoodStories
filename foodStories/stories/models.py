from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Story(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    story_file = models.FileField(_("Story file"), upload_to="partials", max_length=100)
    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE, null=True)

    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True, null = True)

class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    ingredients = models.TextField(_("Ingredients"))
    directions = models.TextField(_("Directions"), default="")
    prepare_time = models.CharField(_("Prepare time"), max_length=50)
    recipe_image = models.ImageField(_("Image"), upload_to='partials/images')

    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True)
    authors = models.ManyToManyField("stories.Author", verbose_name=_("Authors"))
    
    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True)
    
class Author(models.Model):
    first_name = models.CharField(_("Name"), max_length=50)
    last_name = models.CharField(_("Surname"), max_length=50)
    username = models.CharField(_("Username"), max_length=50 , blank=True)
    email = models.EmailField(_("Email"), max_length=254, null=True)
    password = models.CharField(_("Password"), max_length=50, null=True)

class Category(models.Model):
    story_category = models.CharField(_("Story category"), max_length=50 , default='Foods')
    stories = models.ManyToManyField("stories.Story", verbose_name=_("Story"))
    
class Comment(models.Model):
    by = models.CharField(_("By"), max_length=50)
    description = models.TextField(_("Description"))
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)
    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE, blank=True, null=True)
    recipe = models.ForeignKey("stories.Recipe", verbose_name=_("Recipe"), on_delete=models.CASCADE)
    story = models.ForeignKey("stories.Story", verbose_name=_("Story"), on_delete=models.CASCADE, blank=True, null=True)

class Comment_reply(models.Model):
    first_name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    content = models.TextField(_("Message"))
    comment = models.ForeignKey("stories.Comment", verbose_name=_("Comment"), on_delete=models.CASCADE)
    
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)