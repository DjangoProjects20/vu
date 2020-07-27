from django import forms
from django.contrib.auth.models import User # подключаем стандартную таблицу user
from django.contrib.auth.forms import UserCreationForm # автоматическое создание формы
from .models import Profile

class UserOurRegistration(UserCreationForm):# находим стандартную форму и расширяем 
    email = forms.EmailField(required=True)
    #name_spirit = forms.CharField( )
    username = forms.CharField( label='login' )
    
    # последний параметр значит  является данный параметр расширяемым required=True его можно не вводить по умолчанию он True , если написать False то поле емаил будет не обязательным
    
    class Meta: # каким образом мы будем отбражать в форме последовательность 'username', убрали из двух следующих fields
        model = User 
        fields = ['username','email', 'password1', 'password2', ] #'username',
    
    
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
   
    
    class Meta:
        model = User
        fields = [ 'username','email']
        
        
        
"""       
class UserAuth2(forms.ModelForm):
   
    class Meta:
        model = User
        fields = [ 'email','password2' ]    #,'password2'    

"""        
class UserAuth2(forms.Form):
    #username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
        
        
        
class ProfileImage(forms.ModelForm):
    class Meta:
        model = Profile # 'name', 
        fields = [ 'name','pol', 'img', 'familia',  'name_spirit', 'use_spirit_name', 'tel', 'vk_page', 'datebith',  'comment',]
        #fields = '__all__' 

"""        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [ 'username','email']   
        
        
        
        
class UserOurRegistration(UserCreationForm):# находим стандартную форму и расширяем 
    email = forms.EmailField(required=True)
    #name_spirit = forms.CharField( )
    
    # последний параметр значит  является данный параметр расширяемым required=True его можно не вводить по умолчанию он True , если написать False то поле емаил будет не обязательным
    
    class Meta: # каким образом мы будем отбражать в форме последовательность 'username', убрали из двух следующих fields
        model = User 
        fields = [ 'username','password1', 'password2','email', ]
            
    
"""        
