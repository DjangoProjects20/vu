# Generated by Django 2.2 on 2020-06-03 11:31

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog_admin', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='телефон манаджера')),
                ('tel_resption', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='телефон ресепшена')),
                ('email_to_questions', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='email для вопросов')),
                ('adres', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='адрес')),
                ('descrip_how_to_back', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='описание как добраться')),
                ('vk', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='адрес vk')),
                ('instagram', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='instgram')),
                ('inf_for_urist', models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='Юридическая информация')),
                ('access_user', models.ImageField(blank=True, help_text='изображение', upload_to='static/media/img', verbose_name='изображение')),
                ('donnat', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='реквизиты для пожертвований')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='day_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='место проведения')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
            ],
            options={
                'verbose_name': 'день проведения',
                'verbose_name_plural': 'дни проведения',
            },
        ),
        migrations.CreateModel(
            name='inf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя')),
                ('desctip_html', tinymce.models.HTMLField(verbose_name='описание в виде html')),
                ('descrip_text', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='описание в тексте')),
                ('is_active', models.BooleanField(default='True', verbose_name='вкл?')),
                ('img', models.ImageField(blank=True, help_text='изображение', upload_to='static/media/img', verbose_name='фото курса')),
            ],
            options={
                'verbose_name': 'Информацию',
                'verbose_name_plural': 'Информация',
            },
        ),
        migrations.CreateModel(
            name='kurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='Название курса')),
                ('teacher', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='Преподаватель')),
                ('descrip', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='описание')),
                ('img', models.ImageField(blank=True, help_text='изображение', upload_to='static/media/img', verbose_name='фото курса')),
                ('comit_manager', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='комментарии менеджера')),
                ('its_new', models.BooleanField(default='True', verbose_name='вкл?')),
                ('is_active', models.BooleanField(default='True', verbose_name='вкл?')),
                ('num_students', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='десятичное число')),
                ('num_students_ending_kurs', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='десятичное число')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя слайда')),
                ('image', models.ImageField(blank=True, help_text='изображение', upload_to='static/media/img', verbose_name='изображение')),
                ('description', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='описание')),
                ('link', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='ссылка')),
                ('is_active', models.BooleanField(default='True', verbose_name='вкл?')),
                ('active_slide', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='если слайд 1 то active')),
                ('text_button', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='текст кнопки')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='socbutton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя')),
                ('link', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='ссылка')),
                ('icon', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='иконка')),
                ('is_active', models.BooleanField(default='True', verbose_name='вкл?')),
            ],
            options={
                'verbose_name': 'соцкнопка',
                'verbose_name_plural': 'соцкнопки',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='имя')),
                ('two_name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='фамилия')),
                ('spirit_name', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='духовное имя')),
                ('foto', models.ImageField(blank=True, help_text='изображение', upload_to='static/media/img', verbose_name='изображение')),
                ('tel', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='телефон')),
                ('comment_teacher', models.TextField(blank=True, default='', max_length=264, null=True, verbose_name='комментарии преподавателя')),
                ('comment_manager', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='комментарии менеджера')),
                ('is_active', models.BooleanField(default='True', verbose_name='вкл?')),
                ('donat_num', models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='реквизиты для пожертвований')),
                ('num_kurs_event', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='десятичное число')),
                ('donat_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='десятичное число')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='coment_manager',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='комментарий менеджера'),
        ),
        migrations.AddField(
            model_name='profile',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='комменетарии студента'),
        ),
        migrations.AddField(
            model_name='profile',
            name='datebith',
            field=models.DateTimeField(default='2020-01-01', verbose_name='дата'),
        ),
        migrations.AddField(
            model_name='profile',
            name='familia',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='фамилия'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name_spirit',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='духовное имя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tel',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='телефон'),
        ),
        migrations.AddField(
            model_name='profile',
            name='vk_page',
            field=models.CharField(blank=True, default='', max_length=264, null=True, verbose_name='vk'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='categories',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='StudyBlog_admin.Post_categories', verbose_name=' '),
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AddField(
            model_name='day_event',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='StudyBlog_admin.kurs', verbose_name='связь'),
        ),
    ]
