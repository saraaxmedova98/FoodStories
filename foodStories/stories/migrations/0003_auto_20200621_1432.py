# Generated by Django 3.0.6 on 2020-06-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20200621_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover_image',
            field=models.ImageField(default='bg_4.jpg', upload_to='stories', verbose_name='Cover image'),
        ),
    ]