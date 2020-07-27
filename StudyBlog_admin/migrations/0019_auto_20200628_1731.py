# Generated by Django 2.2 on 2020-06-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0018_auto_20200628_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe_course',
            name='pol_student',
            field=models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='пол студента'),
        ),
        migrations.AlterField(
            model_name='name_pol',
            name='name',
            field=models.TextField(blank=True, default='оба', max_length=32, null=True, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='text_msg',
            name='is_active',
            field=models.BooleanField(default='False', verbose_name='включить эту рассылку '),
        ),
    ]
