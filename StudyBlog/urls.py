from django.conf.urls import url, include 
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path 
from django.views.generic import TemplateView
#from django.contrib.auth import views as auth_Views # это псевдоним

admin.site.site_header = "вайшнавский университет"
admin.site.site_title = "вайшнавский университет"
admin.site.index_title = "Добро пожаловать в административную часть сайта"


urlpatterns = [
path('admin/', admin.site.urls),  
url(r'^', include('StudyBlog_admin.urls')), 
   
url(r'^tinymce/', include('tinymce.urls')), 
path(r'robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),name='robots.txt'),
    
#url(r'^auth_user/$', auth_Views.LoginView.as_view(template_name='auth_user.html'), name='auth_user'),
#url(r'^exit_user/$', auth_Views.LogoutView.as_view(template_name='exit_user.html'), name='exit'),
#url(r'^prof/$', views.prof, name='prof'),    
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
