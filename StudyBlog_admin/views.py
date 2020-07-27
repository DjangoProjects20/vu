from django.shortcuts import render , redirect
from . models import *
#from django.contrib.auth.forms import UserCreationForm #это для %%%%% смотри внизу 
from django.contrib import messages
from .forms import UserOurRegistration, ProfileImage, UserUpdateForm,UserAuth2
#+для дикоратора
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
import time
from django.http import HttpResponse

#+ для отпраки почты
from django.core.mail import send_mail
from django.conf import settings
#-

#-для дикоратора

def index(request):
      #Post_categoriess = Post_categories.objects.filter(is_active=True)
      #Postss = Posts.objects.filter(is_active=True)
      #newss = News.objects.all()
      
      return render(request, 'build/index.html', locals())

def first(request):
      #Post_categoriess = Post_categories.objects.filter(is_active=True)
      #Postss = Posts.objects.filter(is_active=True)
      #newss = News.objects.all()
      
      return render(request, 'build/index.html', locals())
    
    
def teachers_page(request):
      teachers = teacher.objects.filter(is_active=True)
      return render(request, 'build/tutors.html', locals())

def teacher_page(request,teacher_id):
      teacher_mass = teacher.objects.get(id=teacher_id)
      return render(request, 'build/tutor.html', locals())     
    

def course(request, course_id):
    course = kurs.objects.get(id=course_id)
    day_event_mass = day_event.objects.filter(is_active= True, date__month = datetime.datetime.now().month, link=course_id) 
    return render(request, 'build/course.html', locals())  

def courses(request):
    courses = kurs.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active =True)
    return render(request, 'build/courses.html', locals())



 
def contacts_page(request):
    return render(request, 'build/contacts.html', locals()) 

 
def time_page(request):
    day_event_mass = day_event.objects.filter(is_active= True, date__month = datetime.datetime.now().month )  
    courses = kurs.objects.filter(is_active=True) 
    return render(request, 'build/schedule.html', locals()) 

def kabinet(request , student_id):
    courses = subscribe_course.objects.filter(id_student = student_id )
    
    return render(request, 'build/cabinet.html', locals()) 

def reg_in_course(request, kurs_id ):
    
    # проверка на регистрацию
    if subscribe_course.objects.filter(id_student = request.user.id ,id_kurs = kurs_id ):
        return HttpResponse("Дорогой студент ты уже есть на этом курсе, Харе Кришна")
    
    user_id = request.user.id # кто регистрируется
    user_name = request.user.profile.name # имя в профаиле из запроса
    course = kurs.objects.get(id=kurs_id)
    #функция регитрации 
    if not subscribe_course.objects.filter(id_student = request.user.id ,id_kurs = kurs_id ):
        subscribe_course.objects.get_or_create(name = course.name ,id_student = user_id ,  name_student = user_name,  id_kurs = kurs_id , is_active = "False" ,status_sub = "True", email_student = request.user.email , pol_student = request.user.profile.pol)
        
        #messages.success(request, f' Пользователь {user_name} был успешно зарегистрирован на курс "{course.name}"')
        messages.info(request, ' Вы успешно добавлены на курс')
        courses = subscribe_course.objects.filter(id_student = user_id)
        return render(request, 'build/cabinet.html', locals()) 
     
   

def glory(request):
    return render(request, 'build/vaishnavaglory.html', locals())
#def del_in_course(request, kurs_id ):
#    
#    user_id = request.user.id # кто регистрируется
#    user_name = request.user.profile.name # имя в профаиле из запроса
#    
#    course = kurs.objects.get(id=kurs_id)
#    
#    #функция регитрации 
#    if subscribe_course.objects.update_or_create(name = course.name ,
#        id_student = user_id,  name_student = user_name,  id_kurs = kurs_id, is_active = "False" , status_sub = "True" ):
#        messages.success(request, f' Пользователь {user_name} был успешно зарегистрирован на курс "{course.name}"')
#        courses = subscribe_course.objects.filter(id_student = user_id  )
#        return render(request, 'build/cabinet.html', locals())    
#    



'''  это вид регистрации без расширения %%%%%
def register(request):
    if request.method == "POST":# если сработал метод пост
        form = UserCreationForm(request.POST)# создаем обьект метода form
        if form.is_valid():#проверяю на валидность форму
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f' Пользователь {username} был успешно создан!')# форматированная строка символ f
            
            # добавить на нужную тебе страницу вывод сообщение об успешной регистрации
            #{%if messages%}
            # {% for mess in messages %}
            # <div class="alert alert-success">
            # {{mess}}
            # </div>
            #{%endfor%}
            #{%endif%}
            return redirect('http://127.0.0.1:8019/index')# настраиваемый редирект
    else:# в другом случае просто создаем форму
        form = UserCreationForm()


    return render(request, 'registration.html', {'form': form, 'title':'регистрация пользователя'})
 '''   


#  это вид регистрации c расширением 
def register(request):
    if request.method == "POST":# если сработал метод пост
        form = UserOurRegistration(request.POST)# создаем обьект метода form
        if form.is_valid():#проверяю на валидность форму
            form.save()
            username = form.cleaned_data.get("username")
            #messages.success(request, f' Пользователь {username} был успешно создан, введите имя пользователя и пароль для авторизации! также Вам необходимо заполинить свои данные в личном кабинете чтобы зарегистрирваться на курсы')# форматированная строка символ f
            messages.success(request, 'Ваш профиль был успешно создан, введите имя пользователя и пароль для авторизации! также Вам необходимо заполинить свои данные в личном кабинете чтобы зарегистрирваться на курсы')# форматированная строка символ f
            
            # добавить на нужную тебе страницу вывод сообщение об успешной регистрации
            #{%if messages%}
            # {% for mess in messages %}
            # <div class="alert alert-success">
            # {{mess}}
            # </div>
            #{%endfor%}
            #{%endif%}
            return redirect('http://www.bhaktivedanta-center.ru/auth_user/')# настраиваемый редирект
    else:# в другом случае просто создаем форму
        form = UserOurRegistration()


    return render(request, 'registration.html', {'form': form, 'title':'регистрация студента'})
    
    
    
    
    
    
    

#  это вид авторизации
def auth_user(request):
    if request.method == "POST":# если сработал метод пост
        form = UserAuth2(request.POST)# создаем обьект метода form
        if form.is_valid():#если форма валидна то
            cd = form.cleaned_data#очищаем форму
            #user = authenticate(username=cd['username'], password=cd['password'])
            
            user_arr = User.objects.get(email = cd['email'] )#делаем выборку для того чтобы узнать имя пользователя для этой почты 
            #print(user_arr.username, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',user_arr.password) 
            #print(cd['password'])
            user_name =user_arr.username #  для метода authenticate нужно вывести в отдельные переменные  
            user_password= cd['password']
            if authenticate(request,username= user_name, password= user_password) : # проверка на ауентичность если прошло то логиним
            		user = authenticate(request,username= user_name, password= user_password) 
            		#print('user is authecated!!!!!!!!!!!!!!!!!!!!')
            		login(request, user)
            		#return HttpResponse('Authenticated successfully')
            		if user.profile.is_verifecieted:
            			messages.error(request, 'Вы успешно авторизировались')# 
            			return redirect('/')
            		else:
            			messages.error(request, 'вам необходимо заполнить профиль для регистрации на курсах')# 
            			return redirect('http://www.bhaktivedanta-center.ru/prof/')	
                
            else:
            	messages.error(request, 'вы неправильно заполнили форму проверьте еще раз правильность')#
            	#return HttpResponse('Invalid login')
            	form = UserAuth2
    else:
        form = UserAuth2

    return render(request, 'auth_user.html', {'form': form, 'title':'авторизация'})   
    
    
 
    
       

#+пример дикоратора
@login_required
def prof(request):
    if request.method == 'POST':
          img_profile = ProfileImage(request.POST, request.FILES,  instance=request.user.profile)
          #update_user = UserUpdateForm(request.POST, instance=request.user)
          if img_profile.is_valid(): #update_user.is_valid() and
          #update_user.save()
                  img_profile.save()
                  messages.success(request, 'Данные обновлены')
                  # проверка заполнения профиля
                  if request.user.profile.name != '' and request.user.profile.tel != '' and request.user.profile.pol != 3 and request.user.profile.img != 'user_images/foto_empty.jpg' and request.user.profile.familia !=''  :
                  	Profile.objects.filter(id = request.user.profile.id ).update(is_verifecieted = True )
                  
                  
                  
                  
                  return redirect('prof/')

    else:  
          img_profile = ProfileImage(instance=request.user.profile)
          #update_user = UserUpdateForm(instance=request.user)
      
    return render(request, 'prof.html', locals())

#-пример дикоратора

# функция заполнения текста в отправку
def load_text_in_sender(request):
    text_msg_for_send_type_kurs = text_msg.objects.get(is_active = True) #сделал выборку из сообщений которые нужно отпавить 
    #print(text_msg_for_send_type_kurs.link , '!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    name_to_load = str(text_msg_for_send_type_kurs.link)
    
    send_type_mass = subscribe_course.objects.filter(name = text_msg_for_send_type_kurs.link.name )#Сделал выборку массив для добавления сообщений
    """ задача в том чтобы сделать выгрузку из бд по имени сохраненом через forigen 
    """
    
    print (send_type_mass)
    for item in send_type_mass:# перебрал в цикле для отправки
        subscribe_course.objects.filter(id = item.id).update(text_email = text_msg_for_send_type_kurs.name)
        print( 'заполнил подпись на курсы у которой id = ' ,item.id )
    return HttpResponse("Сообщения по данному курсу были подготовлены к отправке")    
        
    
# функция заполнения текста в отправку
def load_text_in_mass_sender(request):
    text_msg_for_send_type_kurs = text_msg.objects.filter(is_active = True) #сделал выборку из сообщений которые нужно отпавить 
    for send in text_msg_for_send_type_kurs:
        
        # далее выборки с учетом пола в соответствии с таблицами задачи для отправки, причем обрати внимание переход через связь link_pol
         
        if send.link_pol.name == "оба":
            send_type_mass = subscribe_course.objects.filter(name = send.link.name )    
        if send.link_pol.name == "мужской":
            send_type_mass = subscribe_course.objects.filter(name = send.link.name , pol_student = 1 )    
        if send.link_pol.name == "женский":
            send_type_mass = subscribe_course.objects.filter(name = send.link.name , pol_student = 2 )
        # выборка всех разом     
        if send.link.name == "Все":
            send_type_mass = subscribe_course.objects.all()    
        # далее выборки с учетом пола
        for item in send_type_mass:# перебрал в цикле для отправки
            subscribe_course.objects.filter(id = item.id).update(text_email = send.name,is_active=False)# поменял значения сообщений и подготовил к отпавки
            text_msg.objects.filter(id = send.id).update(is_active=False)#сообщения перевели в неакитвное состояние 
        # далее идет блок отправки по всем адресам     
        sends_mass = subscribe_course.objects.filter(is_active=False)# делаю выборку сообщений которые не отправлены 
        for send in sends_mass: # в цикле отправляю 
            msg = send.text_email
            send_mail(u'', msg , settings.EMAIL_HOST_USER, [send.email_student], fail_silently=False)
            subscribe_course.objects.filter(id = send.id).update(is_active=True)# меняю статусы на отправки на положителные
               
            
            #заполнил подпись на курсы у которой id = ' ,item.id 
    return HttpResponse("Сообщения были отправлены")  




def send_product(request):
    sends_mass = subscribe_course.objects.filter(is_active=False) 
    for send in sends_mass:
        msg = send.text_email
        send_mail(u'', msg , settings.EMAIL_HOST_USER, [send.email_student], fail_silently=False)
        subscribe_course.objects.filter(id = send.id).update(is_active=True)
        send_massege = 'Ваше сообщение(я) отправлены'
    return HttpResponse(send_massege)
