import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-o#zl6zktmm6b!n1pg(nva5*19hgr=y%zg(22r^++m9t(^#=4m'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'StudyBlog_admin.apps.StudyblogAdminConfig',# внимание только так для работы signals
    #'StudyBlog_admin',
    'crispy_forms',
    'tinymce',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'StudyBlog.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'StudyBlog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
{
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = '151.248.121.197'
#META_SITE_DOMAIN = 'www.bhaktivedanta-center.ru'
META_USE_TITLE_TAG = True
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bhaktivedantasentr@gmail.com'
EMAIL_HOST_PASSWORD = '354etrETR'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LANGUAGE_CODE = 'Ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static', ),
)
#STATIC_ROOT = os.path.join(BASE_DIR, 'static',)
MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
#
STATIC_ROOT = '/home/django/vu/static/asset' 
MEDIA_ROOT = '/home/django/vu/media'
#
#



''' + для стилей формы'''
CRISPY_TEMPLATE_PACK = 'bootstrap4'
''' - для стилей формы'''

''' + для перевода на страницу после авторизации '''
LOGIN_REDIRECT_URL = 'index'
#LOGIN_REDIRECT_URL = ''
''' - для перевода на страницу после авторизации '''

''' + переход при логине '''
LOGIN_URL = 'index'
#LOGIN_URL = ''
''' - переход при логине '''




