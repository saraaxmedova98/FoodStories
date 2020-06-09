# Generated by Django 3.0.6 on 2020-06-09 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_auto_20200608_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='comment_reply',
            old_name='content',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='category',
            name='recipe_category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='stories',
        ),
        migrations.RemoveField(
            model_name='category',
            name='story_category',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='by',
        ),
        migrations.RemoveField(
            model_name='comment_reply',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='story',
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Biography'),
        ),
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='partials', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='partials', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.AddField(
            model_name='comment_reply',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='comment_reply',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='story',
            name='story_file',
            field=models.FileField(blank=True, null=True, upload_to='partials', verbose_name='Story file'),
        ),
        migrations.AlterField(
            model_name='comment_reply',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, null=True, upload_to='partials', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('recipes', models.ManyToManyField(to='stories.Recipe', verbose_name='Recipe')),
                ('stories', models.ManyToManyField(to='stories.Story', verbose_name='Story')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='partials', verbose_name='Image')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='Updated date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Author', verbose_name='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Category', verbose_name='Category')),
                ('tags', models.ManyToManyField(to='stories.Tag', verbose_name='Tag')),
            ],
        ),
    ]
