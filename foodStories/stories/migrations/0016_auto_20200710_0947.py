# Generated by Django 3.0.7 on 2020-07-10 09:47

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('stories', '0015_auto_20200710_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggedstory',
            name='content_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='story', to='stories.Story'),
        ),
        migrations.CreateModel(
            name='TaggedRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='stories.Recipe')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories_taggedrecipe_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='stories.TaggedRecipe', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]