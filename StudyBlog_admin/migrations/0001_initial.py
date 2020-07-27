# Generated by Django 2.1.4 on 2019-01-09 06:52

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='имя категории в навигации ')),
                ('description', tinymce.models.HTMLField(default='None', null=True, verbose_name='описание категории сюда можно поместить целую статью в html ')),
                ('image', models.ImageField(blank=True, help_text='загрузите сюда изображение для категории это будет в плитках навигации', upload_to='static/media/categories_images/', verbose_name=' главное изображение для категории')),
                ('is_active', models.BooleanField(default='True', verbose_name='Вкл? ')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='None', max_length=64, null=True, verbose_name='имя статьи кратко это будет в меню навигации')),
                ('description', tinymce.models.HTMLField(blank=True, default='None', null=True, verbose_name=' все описание статьи можно вставлять код html целиком')),
                ('is_active', models.BooleanField(default='True', verbose_name=' выложить статью на сайт ')),
                ('categories', models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post', to='StudyBlog_admin.Post_categories', verbose_name=' ')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]