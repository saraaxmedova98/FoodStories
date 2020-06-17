from django import template
from stories.forms import SubscribeForm
from stories.models import SiteSettings

register = template.Library()

@register.simple_tag
def subscribe_form():
    return SubscribeForm


@register.simple_tag
def site_settings():
    return SiteSettings.objects.get(pk=1)
