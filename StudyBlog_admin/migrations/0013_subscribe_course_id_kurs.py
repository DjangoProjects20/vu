# Generated by Django 2.2 on 2020-06-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0012_subscribe_course_id_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe_course',
            name='id_kurs',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='id курса'),
        ),
    ]
