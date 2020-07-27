# Generated by Django 2.2 on 2020-06-20 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0009_auto_20200615_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя курса')),
                ('name_student', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя студента который записался')),
                ('email_student', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='email студента для отправки рассылки')),
                ('is_active', models.BooleanField(default='True', verbose_name='добавление в рассылку')),
                ('status_sub', models.BooleanField(default='True', verbose_name='студент подписан на этот курс')),
            ],
            options={
                'verbose_name': 'запись на курс',
                'verbose_name_plural': 'записи на курсы',
            },
        ),
    ]