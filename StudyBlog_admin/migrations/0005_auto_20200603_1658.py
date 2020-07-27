# Generated by Django 2.2 on 2020-06-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0004_auto_20200603_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_event',
            name='date',
            field=models.DateTimeField(verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='is_active',
            field=models.BooleanField(default='True', verbose_name='Это активный курс'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='its_new',
            field=models.BooleanField(default='True', verbose_name='это новый курс?'),
        ),
    ]