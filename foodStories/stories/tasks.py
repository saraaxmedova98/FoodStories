
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from stories.models import Story, Subscribe
from django.template.loader import render_to_string
import datetime

@shared_task
def add(x, y):
    return x + y

@shared_task
def subscribers_email():
    
    subject = 'Hello, This is new Stories'
    subscribers = list(Subscribe.objects.values_list('email' , flat = True))
    text_content = 'This is an important message.'
    from_email = 'ahmadovasara@yandex.ru'
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    content = Story.objects.filter(created_at__gt = yesterday)
    html_content = render_to_string('email_subscribers.html' , { 'context' : content, 'user' : subscribers })
    msg = EmailMultiAlternatives(subject, text_content, from_email, subscribers)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    