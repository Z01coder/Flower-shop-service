"""
Настройки Django для проекта flower_shop.

Сгенерировано командой 'django-admin startproject' с использованием Django 5.1.5.

Дополнительные сведения об этом файле см.
https://docs.djangoproject.com/en/5.1/topics/settings/

Полный список настроек и их значений приведен в разделе
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Создавайте пути внутри проекта следующим образом: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Загрузка переменных окружения из .env файла
load_dotenv()

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Настройки быстрого запуска разработки - непригодны для производства
# Смотрите https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# ПРЕДУПРЕЖДЕНИЕ ПО ТЕХНИКЕ БЕЗОПАСНОСТИ: берегите секретный ключ, используемый в продакшене!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-lr&2mbpvij%37pv@q^th!9vbh*uj8@i!za_oon=*m04)4pbxi!')
if SECRET_KEY == 'django-insecure-lr&2mbpvij%37pv@q^th!9vbh*uj8@i!za_oon=*m04)4pbxi!':
    import warnings
    warnings.warn(
        'Используется небезопасный SECRET_KEY по умолчанию. '
        'Установите SECRET_KEY в переменных окружения для продакшена!',
        UserWarning
    )

# ВНИМАНИЕ: не запускайте приложение с включённой отладкой в рабочей среде!
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if os.getenv('ALLOWED_HOSTS') else []


# Определение приложений
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flower_shop.apps.OrdersConfig',
    'pytest_django',
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

ROOT_URLCONF = 'flower_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'flower_shop.wsgi.application'


# Базы данных
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Проверка пароля
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Интернационализация
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, изображения)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'flower_shop.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = '/login/'

# Telegram bot
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_ADMIN_CHAT_ID = os.getenv('TELEGRAM_ADMIN_CHAT_ID', '')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        # Отключаем логирование HTTP запросов от telegram и httpx
        'httpx': {
            'handlers': ['console'],
            'level': 'WARNING',  # Показываем только предупреждения и ошибки
            'propagate': False,
        },
        'telegram': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}