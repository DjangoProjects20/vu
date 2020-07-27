# Generated by Django 2.2 on 2020-06-04 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0007_kurs_teacher_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'студент', 'verbose_name_plural': 'студенты'},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name_spirit',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='kurs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='StudyBlog_admin.kurs', verbose_name='на каких курсах'),
        ),
    ]