# Generated by Django 3.0.6 on 2020-06-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20200606_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='age',
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default='', verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
