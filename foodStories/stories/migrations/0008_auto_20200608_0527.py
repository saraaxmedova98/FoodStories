# Generated by Django 3.0.6 on 2020-06-08 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_auto_20200608_0525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='stories',
            new_name='story',
        ),
    ]