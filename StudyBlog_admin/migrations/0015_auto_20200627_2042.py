# Generated by Django 2.2 on 2020-06-27 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0014_auto_20200624_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='name_kurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='None', max_length=4096, null=True, verbose_name=' имя курса ')),
            ],
            options={
                'verbose_name': 'имя курса для рассылки',
                'verbose_name_plural': 'имя курса для рассылки',
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='kur_end',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='kur_regs',
        ),
        migrations.AlterField(
            model_name='subscribe_course',
            name='is_active',
            field=models.BooleanField(default='False', verbose_name='сообщение отправлены?'),
        ),
        migrations.AlterField(
            model_name='text_msg',
            name='is_active',
            field=models.BooleanField(default='False', verbose_name='включить эту рассылку, внимание включить можно только одну рассылку '),
        ),
        migrations.AddField(
            model_name='text_msg',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='StudyBlog_admin.name_kurs', verbose_name='имя курса'),
        ),
    ]
