# Generated by Django 2.2 on 2020-06-15 12:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0008_auto_20200604_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='kurs',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='donat_sum',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='num_kurs_event',
        ),
        migrations.AddField(
            model_name='day_event',
            name='date2',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата конца'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='tag',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='теги'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='profile',
            name='kur_end',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='список курсов которые прошел'),
        ),
        migrations.AddField(
            model_name='profile',
            name='kur_regs',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='список курсов на которые зарегистрирован'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name_spirit',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя духовное'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pol',
            field=models.IntegerField(choices=[(1, 'Мужской'), (2, 'Женский'), (3, 'нужно выбрать')], default='3', verbose_name='пол'),
        ),
        migrations.AddField(
            model_name='profile',
            name='use_spirit_name',
            field=models.BooleanField(default='False', verbose_name='использовать духовное имя как основное'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email_teacher',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='inf_about_teacher',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='информация о преподавателе'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='soc_about_teacher',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='соцсети преподавателя'),
        ),
        migrations.AlterField(
            model_name='day_event',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата начала'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='comit_manager',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='комментарии менеджера'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='descrip',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='is_active',
            field=models.BooleanField(default='True', verbose_name='активный курс'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='its_new',
            field=models.BooleanField(default='True', verbose_name='новый курс'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='num_students',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='зарегистрировашиеся '),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='num_students_ending_kurs',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='прошедшие'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='teacher',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='Комментарии преподавателя'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='teacher_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kurs', to='StudyBlog_admin.teacher', verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='coment_manager',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='комментарий менеджера'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='comment',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='комменетарии студента'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='datebith',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='user_images/foto_empty.jpg', upload_to='user_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='comment_manager',
            field=models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='комментарии менеджера'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_active',
            field=models.BooleanField(default='True', verbose_name='Действующий'),
        ),
    ]
