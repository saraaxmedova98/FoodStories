
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from stories.models import Story, Subscribe
from django.template.loader import render_to_string
import datetime
from django.contrib.auth import get_user_model
from django.http import HttpResponse , JsonResponse
import xlwt

User = get_user_model()


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

@shared_task
def export_users_xls():
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    # return response