from django.db import models
from django.utils.translation import gettext as _
import datetime
# Create your models here.

class Story(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE, null=True)

    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True, null = True)

class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), default='')
    ingredients = models.TextField(_("Ingredients"))
    directions = models.TextField(_("Directions"), default="")
    prepare_time = models.TimeField(_("Prepate time"), default= datetime.time(16, 00))
    recipe_image = models.ImageField(_("Image"), upload_to='partials/images')

    authors = models.ManyToManyField("stories.Author", verbose_name=_("Authors"))
    stories = models.ForeignKey("stories.Story", verbose_name=_("Story"), on_delete=models.CASCADE, null=True)

    updated_at = models.DateField(_("Updated date"), auto_now=True)
    created_at = models.DateField(_("Created date"), auto_now_add=True)
    
class Author(models.Model):
    first_name = models.CharField(_("Name"), max_length=50)
    last_name = models.CharField(_("Surname"), max_length=50)
    experience = models.IntegerField(_("Experience"))
    bio = models.TextField(_("Biography"), default="")
    graduated_from = models.CharField(_("Graduated"), max_length=50)

class Category(models.Model):
    recipe_category = models.CharField(_("Recipe category"), max_length=50)
    recipes = models.ManyToManyField("stories.Recipe", verbose_name=_("Recipes"))
    
class Comment(models.Model):
    by = models.CharField(_("By"), max_length=50)
    description = models.TextField(_("Description"))
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)
    recipe = models.ForeignKey("stories.Recipe", verbose_name=_("Recipe"), on_delete=models.CASCADE)

class Comment_reply(models.Model):
    first_name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    message = models.TextField(_("Message"))
    comment = models.ForeignKey("stories.Comment", verbose_name=_("Comment"), on_delete=models.CASCADE)
    
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)