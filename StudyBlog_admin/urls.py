from django.conf.urls import url, include
from . import views
from django.contrib import admin 
from django.urls import path
#+авторизация пользователя подключение и потом добавляю в url
from django.contrib.auth import views as auth_Views # это псевдоним
#-авторизация пользователя подключение и потом добавляю в url



urlpatterns = [
    
    
#url(r'^auth_user/', auth_Views.LoginView.as_view(template_name='auth_user.html'), name='auth_user'),
url(r'^auth_user/', views.auth_user, name='auth_user'),

url(r'^exit_user/', auth_Views.LogoutView.as_view(template_name='exit_user.html'), name='exit'),
url(r'^prof/', views.prof, name='prof'),
#path('admin/', admin.site.urls),  
url(r'^register/', views.register, name='register'),
#+авторизация пользователя    

url(r'^course_page/(?P<course_id>\w+)/', views.course, name='course_page'),      
url(r'^courses_page', views.courses, name='courses_page'),     
url(r'^teachers_page', views.teachers_page, name='teachers_page'),   
url(r'^teacher_page/(?P<teacher_id>\w+)/', views.teacher_page, name='teacher_page'),   
url(r'^$', views.first, name=''), 
url(r'^index$', views.index, name='index'),
    
url(r'^contacts', views.contacts_page, name='contacts'),
url(r'^time_page', views.time_page, name='time_page'),
    
url(r'^kabinet/(?P<student_id>\w+)/', views.kabinet, name='kabinet'),     
   
url(r'^reg_in_course/(?P<kurs_id>\w+)/', views.reg_in_course, name='reg_in_course'),   
    
    
url(r'^glory', views.glory, name='glory'),    
 
    
url(r'^send_product', views.send_product, name='send_product'),    
url(r'^load_text_in_sender', views.load_text_in_sender, name='load_text_in_sender'),
url(r'^load_text_in_mass_sender', views.load_text_in_mass_sender, name='load_text_in_mass_sender'), 
   
   


    
#-авторизация пользователя
    
#c параметром Post_categories
#url(r'^Post_categories_page/(?P<Post_categories_id>\w+)/', views.Post_categories_view, name='Post_categories_page'),
#c параметром Posts
#url(r'^Posts_page/(?P<Posts_id>\w+)/', views.Posts_view, name='Posts_page'),
#без параметра Post_categories
#url(r'^Post_categories_page', views.Post_categories_view, name='Post_categories_page'),
#без параметра Posts
#url(r'^Posts_page', views.Posts_view, name='Posts_page'),
]
