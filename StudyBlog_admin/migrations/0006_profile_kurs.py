# Generated by Django 2.2 on 2020-06-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0005_auto_20200603_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='kurs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='StudyBlog_admin.kurs', verbose_name='связь'),
        ),
    ]
