from django import template
from stories.forms import SubscribeForm
from stories.models import *
import datetime
register = template.Library()

@register.simple_tag
def subscribe_form():
    return SubscribeForm


@register.simple_tag
def site_settings():
    return SiteSettings.objects.last()

@register.simple_tag()
def stories_count():
    
    return Story.objects.all().count()

@register.simple_tag()
def recipes_count():

    return Recipe.objects.all().count()

@register.simple_tag()
def recipe_count():
    created_list = []
    for recipe in Recipe.objects.all():
        created_list.append(recipe.recipe_count)
    return created_list

@register.simple_tag()
def story_count():
    created_list = []
    for story in Story.objects.order_by('-story_count')[:4]:
        created_list.append(story.story_count)
    return created_list



@register.simple_tag()
def story_title():
    
    return Story.objects.all()

@register.simple_tag()
def recipe_title():
    
    return Recipe.objects.all()
