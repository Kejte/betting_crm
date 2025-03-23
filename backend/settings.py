from pathlib import Path
from environs import Env
from celery.schedules import crontab

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env.str('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', ['*'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django.contrib.postgres',
    'profiles.apps.ProfilesConfig',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'payments.apps.PaymentsConfig',
    'feedback.apps.FeedbackConfig',
    'django_celery_beat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'backend.middlewares.SecretKeyMiddleware'
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME', 'crm'),
        'USER': env.str('DB_USER', 'root'),
        'PASSWORD': env.str('DB_PASSWORD', 'root'),
        'HOST': env.str('DB_HOST', 'db'),
        'PORT': env.str('DB_PORT', '5432'),
        'DISABLE_SERVER_SIDE_CURSORS': True,
        'CONN_HEALTH_CHECKS': True,
        'CONN_MAX_AGE': 0,
    }
}



# Password validation
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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'

# MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SPECTACULAR_SETTINGS = {
    'TITLE': 'Crm',
    'DESCRIPTION': 'Coolest online portfolio service. Now with API:)',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DATETIME_FORMAT': "%d-%m-%Y %H:%M",
}

STATIC_URL = 'static/'
STATIC_ROOT = '/static'

CELERY_BROKER_URL = env.str("REDIS_URL")  
CELERY_RESULT_BACKEND = env.str("REDIS_URL")



CELERY_BEAT_SCHEDULE = {
    "update_expired_payments": {
        "task": "payments.tasks.update_expired_payments",
        "schedule": crontab(minute="*"),
    },
}