# Generated by Django 3.0.7 on 2020-07-01 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200701_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyimage',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='stories.Story'),
        ),
    ]