from django.contrib import admin 
from . models import *
''' + для поля автор в модели новости'''
from django.contrib.auth.models import User
''' - для поля автор в модели новости'''

"""  Модель Post_categories 
class PostsInline(admin.TabularInline):
      model = Posts
      extra = 0

class Post_categoriesAdmin (admin.ModelAdmin):
      list_display = [field.name for field in Post_categories._meta.fields]
      inlines = [PostsInline,]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = Post_categories
admin.site.register(Post_categories, Post_categoriesAdmin )
""" 

"""  Модель Posts 
class PostsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in Posts._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = Posts
admin.site.register(Posts, PostsAdmin )
""" 



"""  Модель Posts 
class name_kursAdmin (admin.ModelAdmin):
      list_display = [field.name for field in name_kurs._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = name_kurs
admin.site.register(name_kurs, name_kursAdmin )
"""

"""  Модель News  пример который я уже изучал 
class NewsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in News._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = Posts
admin.site.register(News, NewsAdmin )
""" 


#admin.site.register(Profile)

"""  Модель slider 
class sliderAdmin (admin.ModelAdmin):
      list_display = [field.name for field in slider._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = slider
admin.site.register(slider, sliderAdmin )
""" 

"""  Модель news 
class newsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in news._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = news
admin.site.register(news, newsAdmin )
""" 

"""  Модель socbutton 
class socbuttonAdmin (admin.ModelAdmin):
      list_display = [field.name for field in socbutton._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = socbutton
admin.site.register(socbutton, socbuttonAdmin )
""" 

"""  Модель inf """
class infAdmin (admin.ModelAdmin):
      list_display = [field.name for field in inf._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = inf
admin.site.register(inf, infAdmin )
""" конец модели inf"""


# ''' для объедениения полей в админке'''
# class kursInline(admin.TabularInline):
#  model = kurs
#  extra = 0
"""  Модель teacher """
class teacherAdmin (admin.ModelAdmin):
      list_display = [field.name for field in teacher._meta.fields]
#       inlines = [kursInline]    
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = teacher
admin.site.register(teacher, teacherAdmin )
""" конец модели teacher"""



''' для объедениения полей в админке'''
class day_eventInline(admin.TabularInline):
 model = day_event
 extra = 0
#
#''' для объедениения полей в админке'''
#class ProfileInline(admin.TabularInline):
# model = Profile
# extra = 0



"""  Модель kurs """
class kursAdmin (admin.ModelAdmin):
      list_display = [field.name for field in kurs._meta.fields]
      inlines = [day_eventInline]#'ProfileInline']    
      #fields = []
    
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = kurs
admin.site.register(kurs, kursAdmin )
""" конец модели kurs"""

"""  Модель day_event 
class day_eventAdmin (admin.ModelAdmin):
      list_display = [field.name for field in day_event._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = day_event
admin.site.register(day_event, day_eventAdmin )
""" 



"""  Модель contacts """
class contactsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in contacts._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = contacts
admin.site.register(contacts, contactsAdmin )
""" конец модели contacts"""




"""  Модель contacts """
class ProfileAdmin (admin.ModelAdmin):
      list_display = [field.name for field in Profile._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = Profile
admin.site.register(Profile, ProfileAdmin )
""" конец модели contacts"""

''' Модель subscribe_course'''

class subscribe_courseAdmin (admin.ModelAdmin):
      list_display = [field.name for field in subscribe_course._meta.fields]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = subscribe_course

admin.site.register(subscribe_course, subscribe_courseAdmin )
''' конец Модели subscribe_course'''

"""  Модель text_msg """


class text_msgAdmin (admin.ModelAdmin):
      list_display = [field.name for field in text_msg._meta.fields]
      list_editable = ('link','name','link_pol','is_active')   
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = text_msg
admin.site.register(text_msg, text_msgAdmin )
""" конец модели text_msg"""


""" пол
class name_polAdmin (admin.ModelAdmin):
      list_display = [field.name for field in name_pol._meta.fields]   
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = name_pol
admin.site.register(name_pol, name_polAdmin )
"""





