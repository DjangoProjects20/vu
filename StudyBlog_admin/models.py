from tinymce.models import HTMLField 
from django.db import models 
from datetime import datetime   
from PIL import Image
''' + для времени'''
from django.utils import timezone
''' - для времени'''
''' + для поля автор в модели новости'''
from django.contrib.auth.models import User
''' - для поля автор в модели новости'''

""" begin Post_categories"""
class Post_categories(models.Model):
      name =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'имя категории в навигации ')
      description =  HTMLField(   blank=False,  null=True, default='None', verbose_name= 'описание категории сюда можно поместить целую статью в html ')
      image =  models.ImageField(  blank=True,  upload_to='static/media/categories_images/', help_text = 'загрузите сюда изображение для категории это будет в плитках навигации',  verbose_name= ' главное изображение для категории')
      is_active =  models.BooleanField(      default='True', verbose_name= 'Вкл? ')
      def __str__(self):
        return "Категория: %s" % (self.name)
      class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
""" begin Posts"""
class Posts(models.Model):
      name =  models.CharField(  max_length = 64, blank=True,  null=True, default='None', verbose_name= 'имя статьи кратко это будет в меню навигации')
      description =  HTMLField(   blank=True,  null=True, default='None', verbose_name= ' все описание статьи можно вставлять код html целиком')
      categories =  models.ForeignKey(Post_categories, on_delete=models.CASCADE, related_name = 'post', blank=True,  null=True, default='None', verbose_name= ' ')
      is_active =  models.BooleanField(      default='True', verbose_name= ' выложить статью на сайт ')
      def __str__(self):
        return "Статья: %s" % (self.name)
      class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        
        

    

""" begin slider"""
class slider(models.Model):
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'имя слайда')
      image =  models.ImageField(blank=True,upload_to='static/media/img', help_text = 'изображение',   verbose_name=  'изображение')
      description =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'описание')
      link =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'ссылка')
      is_active =  models.BooleanField(default='True', verbose_name= 'вкл?')
      active_slide =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'если слайд 1 то active')
      text_button =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'текст кнопки')
      def __str__(self):
        return "Слайд: %s" % (self.name)
      class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
""" begin news
class news(models.Model):
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'имя')
      description =  HTMLField(verbose_name= 'описание')
      icon =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'иконка')
      is_active =  models.BooleanField(default='True', verbose_name= 'вкл?')
      text =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'описание простым текстом')
      icon =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'иконка с fonteawesome')
      def __str__(self):
        return "Новости: %s" % (self.name)
      class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новость"
"""         
""" begin socbutton"""
class socbutton(models.Model):
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'имя')
      link =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'ссылка')
      icon =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'иконка')
      is_active =  models.BooleanField(default='True', verbose_name= 'вкл?')
      def __str__(self):
        return "соцкнопка: %s" % (self.name)
      class Meta:
        verbose_name = "соцкнопка"
        verbose_name_plural = "соцкнопки"
""" begin inf"""
class inf(models.Model):
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'имя')
      desctip_html =  HTMLField(verbose_name= 'описание в виде html')
      descrip_text =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'описание в тексте')
      is_active =  models.BooleanField(default='True', verbose_name= 'вкл?')
      img =  models.ImageField(blank=True,upload_to='static/media/img', help_text = 'изображение',   verbose_name=  'фото курса')
      def __str__(self):
        return "Информацию: %s" % (self.name)
      class Meta:
        verbose_name = "Информацию"
        verbose_name_plural = "Информация"


""" begin teacher"""
class teacher(models.Model):
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'имя')
      two_name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'фамилия')
      spirit_name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'духовное имя')
      email_teacher =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'email')
      foto =  models.ImageField(blank=True,upload_to='static/media/img', help_text = 'изображение',   verbose_name=  'изображение')
      tel =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'телефон')
      soc_about_teacher =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'соцсети преподавателя')
      inf_about_teacher =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'информация о преподавателе')
      comment_teacher =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'комментарии преподавателя')
      comment_manager =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'комментарии менеджера')
      is_active =  models.BooleanField(default='True', verbose_name= 'Действующий')
      donat_num =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'реквизиты для пожертвований')
      #num_kurs_event =  models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name=  'проведено занятий')
      #donat_sum =  models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=  'собрано пожертвований')
      def __str__(self):
        return " %s" % (self.name)
      class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
            
""" begin kurs"""
class kurs(models.Model):
      teacher_link = models.ForeignKey(teacher, on_delete=models.SET_NULL, related_name = 'kurs',   null=True, verbose_name= 'Преподаватель')
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'Название курса')
      tag = models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'теги')
      teacher =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'Комментарии преподавателя')
      descrip =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'описание')
      img =  models.ImageField(blank=True,upload_to='static/media/img', help_text = 'изображение',   verbose_name=  'фото курса')
      comit_manager =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'комментарии менеджера')
      its_new =  models.BooleanField(default='True', verbose_name= 'новый курс')
      is_active =  models.BooleanField(default='True', verbose_name= 'курс активен')
      num_students =  models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name=  'зарегистрировашиеся ')
      num_students_ending_kurs =  models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name=  'прошедшие')
      
      def __str__(self):
        return "курс: %s" % (self.name)
      class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        
       # вариант пост сеиф 
      def save(self, *args, **kwargs):
         name_kurs.objects.update_or_create(name = self.name )
         
         super(kurs, self).save(*args, **kwargs) 
        
        
        
""" begin day_event"""
class day_event(models.Model):
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'место проведения')
      date =  models.DateTimeField(auto_now_add=False, auto_now=False,blank=True, null=True,  verbose_name=  'дата начала')
      date2 =  models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True,   verbose_name=  'дата конца')
      link =  models.ForeignKey(kurs, on_delete=models.SET_NULL, related_name = 'item',   null=True, verbose_name= 'связь')
      is_active =  models.BooleanField(default='True', verbose_name= 'активно')
      def __str__(self):
        return "день проведения: %s" % (self.name)
      class Meta:
        verbose_name = "день проведения"
        verbose_name_plural = "дни проведения"        
        
""" begin contacts"""
class contacts(models.Model):
      name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'телефон манаджера')
      tel_resption =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'телефон ресепшена')
      email_to_questions =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'email для вопросов')
      adres =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'адрес')
      descrip_how_to_back =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'описание как добраться')
      vk =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'адрес vk')
      instagram =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'instgram')
      inf_for_urist =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'Юридическая информация')
      access_user =  models.ImageField(blank=True,upload_to='static/media/img', help_text = 'изображение',   verbose_name=  'изображение')
      donnat =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'реквизиты для пожертвований')
      def __str__(self):
        return "Контакт: %s" % (self.name)
      class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    
class Profile(models.Model):
#        kur_regs =  models.CharField(max_length = 1000, blank=True,   null=True, default='', verbose_name= 'список курсов на которые зарегистрирован')
#        kur_end =  models.CharField(max_length = 1000, blank=True,   null=True, default='', verbose_name= 'список курсов которые прошел')     
        name =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'имя')
        POL_TYPES=((1,'Мужской'),(2,'Женский'),(3,'нужно выбрать'))   
        pol =  models.IntegerField( verbose_name= 'пол' , default='3',  choices=POL_TYPES)    
        #kurs =  models.ForeignKey(kurs, on_delete=models.SET_NULL, related_name = 'students',   null=True, verbose_name= 'на каких курсах')
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        img = models.ImageField( upload_to='user_images',default='user_images/foto_empty.jpg', )
        familia =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'фамилия')
        name_spirit =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'имя духовное')
        use_spirit_name =  models.BooleanField(default='False', verbose_name= 'использовать духовное имя как основное')   
#        email =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'email')
        tel =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'телефон')
        vk_page =  models.CharField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'vk')
        datebith =  models.DateTimeField(auto_now_add=False, auto_now=False, default=datetime.now,   verbose_name=  'день рождения')    
        comment =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'комменетарии студента')
        coment_manager =  models.TextField(max_length = 264, blank=True,   null=True, default='', verbose_name= 'комментарий менеджера')
        is_verifecieted =  models.BooleanField(default='False', verbose_name= 'профиль прошел верификацию')
        def __str__(self):
            return "студент: %s" % (self.name)
      
#         def save(self):
#                   super().save()
#                   image = Image.open(self.img.path)
#                   if image.height > 256 or image.widht > 256:
#                         resize = (256,256)
#                         image.thumbnail(resize)
#                         image.save(self.img.path)
        class Meta:
            verbose_name = "студент"
            verbose_name_plural = "студенты"
    
class subscribe_course(models.Model):
      name = models.CharField(max_length = 264, blank=True, null=True, default='', verbose_name= 'имя курса' )
      id_kurs = models.CharField(max_length = 264, blank=True, null=True, default='', verbose_name= 'id курса' )    
      name_student = models.CharField(max_length = 264, blank=True, null=True, default='', verbose_name= 'имя студента который записался' )
      id_student = models.CharField(max_length = 264, blank=True, null=True, default='', verbose_name= 'id студента' )
      email_student = models.CharField(max_length = 264, blank=True, null=True, default='', verbose_name= 'email студента для отправки рассылки' )
      pol_student = models.CharField(max_length = 32, blank=True, null=True, default='', verbose_name= 'пол студента' )    
      is_active = models.BooleanField(default='False', verbose_name= 'сообщение отправлены?' )
      text_email =  models.TextField(max_length = 1048, blank=True,   null=True, default='', verbose_name= 'текст рассылки')
      status_sub = models.BooleanField(default='True', verbose_name= 'студент подписан на этот курс' )
      def __str__(self):
       return "запись на курс: %s" % (self.name)
      class Meta:
        verbose_name = 'запись на курс'
        verbose_name_plural = 'записи на курсы'
        
        
""" begin text_msg"""
class name_kurs(models.Model):
      name = models.TextField(  max_length = 4096, blank=True,  null=True, default='None', verbose_name= ' имя курса ')
      def __str__(self):
        return " %s" % (self.name)
      class Meta:
        verbose_name = "имя курса для рассылки"
        verbose_name_plural = "имя курса для рассылки" 
        
""" begin пол"""
class name_pol(models.Model):
      name = models.TextField(  max_length = 32, blank=True,  null=True, default='оба', verbose_name= 'пол')
      def __str__(self):
        return " %s" % (self.name)
      class Meta:
        verbose_name = "пол"
        verbose_name_plural = "пол"
        
           
""" begin text_msg"""
class text_msg(models.Model):
      link =  models.ForeignKey(name_kurs, on_delete=models.SET_NULL, related_name = 'item',   null=True, verbose_name= 'имя курса в которые вы хотите добавить сообщения')
      link_pol =  models.ForeignKey(name_pol, on_delete=models.SET_NULL, related_name = 'item',   null=True,blank=True, verbose_name= 'пол')    
      name = models.TextField(  max_length = 4096, blank=True,  null=True, default='', verbose_name= ' текст для отправки ')
      #discription = HTMLField(blank=True, null=True, default=None ,      verbose_name= ' текст для рассылки ')
      is_active = models.BooleanField(  default='False', verbose_name= 'включить эту рассылку ')
          
      def __str__(self):
        return "Задачи для рассылки: %s" % (self.name)
      class Meta:
        verbose_name = "Задачю для рассылки"
        verbose_name_plural = "Задачи для рассылки"
        
   
