# Generated by Django 3.0.6 on 2020-06-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0018_auto_20200616_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='Recipe Image'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='recipes',
            field=models.ManyToManyField(related_name='stories', to='stories.Recipe', verbose_name='Recipe'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='stories',
            field=models.ManyToManyField(related_name='stories', to='stories.Story', verbose_name='Story'),
        ),
    ]
