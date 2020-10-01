from django import template
from stories.forms import SubscribeForm
from stories.models import *
import datetime
import re
from django.utils.safestring import SafeData, SafeString, mark_safe
register = template.Library()

@register.filter
def highlight_search(text, search):
    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return f'<span class="highlight">{word.upper()}</span>'
            elif text.islower():
                return f'<span class="highlight">{word.lower()}</span>'
            elif text[0].isupper():
                return f'<span class="highlight">{word.capitalize()}</span>'
            else:
                return f'<span class="highlight">{word}</span>'
        return replace

    highlighted = re.sub(search, matchcase(search), text, flags=re.IGNORECASE)
    
    return mark_safe(highlighted)


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


