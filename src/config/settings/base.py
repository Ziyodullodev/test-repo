# from pathlib import Path
import os

import environ

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = env("DEBUG")
BASE_URL = env("BASE_URL")

# AUTH_USER_MODEL = 'users.User'  # use our custom User model (not Django's)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party apps
    'corsheaders',
    'rest_framework',
    'django_filters',
    'drf_spectacular',

    # own apps
    'apps.utils',
    'apps.users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        }
    }
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'api.pagination.CustomPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'login': '5/day',
    },
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # 'UNAUTHENTICATED_USER': 'users.models.AnonymousUser',
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'Service API',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX_INSERT': '/api',
    'ENUM_NAME_OVERRIDES': {
    },
    'SERVE_URLCONF': 'api.urls',
    # OTHER SETTINGS
    'COMPONENT_SPLIT_REQUEST': True
}

SPECTACULAR_SETTINGS_ADMIN = {
    'TITLE': 'Service ADMIN API',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX_INSERT': '/api/admin',
    'ENUM_NAME_OVERRIDES': {
    },
    'SERVE_URLCONF': 'api.admin.urls',
    'DEFAULT_GENERATOR_CLASS': 'config.swaggers.custom_generator.CustomSchemaGenerator',
    # OTHER SETTINGS
}

SPECTACULAR_SETTINGS_CLIENT = {
    'TITLE': 'Service Client API',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX_INSERT': '/api/client',
    'ENUM_NAME_OVERRIDES': {
    },
    'SERVE_URLCONF': 'api.client.urls',
    'DEFAULT_GENERATOR_CLASS': 'config.swaggers.custom_generator.CustomSchemaGenerator',
    # OTHER SETTINGS
}

SPECTACULAR_SETTINGS_MERCHANT = {
    'TITLE': 'Service Merchant API',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX_INSERT': '/api/merchant',
    'ENUM_NAME_OVERRIDES': {
    },
    'SERVE_URLCONF': 'api.merchant.urls',
    'DEFAULT_GENERATOR_CLASS': 'config.swaggers.custom_generator.CustomSchemaGenerator',
    # OTHER SETTINGS
}
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

AUTH_USER_MODEL = 'users.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CORS_REPLACE_HTTPS_REFERER = False
# HOST_SCHEME = "https://"
# SECURE_PROXY_SSL_HEADER = None
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# SECURE_HSTS_SECONDS = None
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# SECURE_FRAME_DENY = False

CORS_ALLOW_CREDENTIALS = True
# If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
# CELERY
# CELERY_APP_NAME = ''
#
# CELERY_BROKER_URL = 'redis://redis_br:6379/0'
# CELERY_RESULT_BACKEND = 'redis://redis_br:6379/0'
#
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_IGNORE_RESULT = False
# CELERYD_TASK_SOFT_TIME_LIMIT = 60
#
# CELERY_ENABLED = True

