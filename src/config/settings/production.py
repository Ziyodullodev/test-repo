from .base import *
from datetime import timedelta

DEBUG = False

# INSTALLED_APPS += [
    # third-parties
# ]

# ALLOWED_HOSTS = [
#     '127.0.0.1',
#     'localhost',
#     '95.169.201.84'
# ]
# print("Production settings")
ALLOWED_HOSTS = ['*']

MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware', ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=60),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "CONN_MAX_AGE": 60,
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    # "https://barakat.ziyodev.uz",
    # "http://barakat.ziyodev.uz",
    # "https://www.barakat.ziyodev.uz",
    # "https://barakat-frontend.ziyodev.uz",
    # "http://barakat-frontend.ziyodev.uz",
]
