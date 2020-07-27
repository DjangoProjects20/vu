#как делать сигнал 
# 1 портируем все бд котроые нужны для работы
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save # далее метод который улавливает сохранение
from django.dispatch import receiver # получатель

@receiver(post_save, sender = User) # когда идет сохранение в таблицу User
def create_profile(sender, instance, created, **kwards):
        if created:
            Profile.objects.create(user=instance) # то в профаил идет сохранение
            
@receiver(post_save, sender = User) # когда идет сохранение в таблицу User
def save_profile(sender, instance, created, **kwards):
     #print( " прошло сохранение в таблицу profile")
     instance.profile.save()  # если user был просто сохранен то и профаил будет сохранен
    

    
# в app обязательно сохранять
# следующее


"""
def ready(self):
    import users.signals
"""    
            
