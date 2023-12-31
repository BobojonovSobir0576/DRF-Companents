from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p_@0$fqrb!kl+d2s2#24!a&d8(lqfca96mojxip0#0**6&6hte'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    'authentification',
    'chat',
    'notification',

    'fitness',

    'find_clinic',


    # other apps
    'django.contrib.sites', 
    'dj_rest_auth',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',
    'rest_framework.authtoken',
    'dj_rest_auth.registration',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

SITE_ID = 1 
ROOT_URLCONF = 'config.urls'

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

# WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = "config.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "companents",
        "USER": "postgres",
        "PASSWORD": "1",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

MEDIA_URL = "/media/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'NON_FIELD_ERRORS_KEY': 'errors',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,


    'AUTH_HEADER_TYPES': ('Bearer','Token'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

FRONTEND_URL = 'http://localhost:5174'


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://localhost:5174",
    FRONTEND_URL
]

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "JWT [Bearer {JWT}]": {
            "name": "Authorization",
            "type": "apiKey",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
}

AUTH_USER_MODEL = "authentification.CustomUser"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sobirbobojonov2000@gmail.com'
EMAIL_HOST_PASSWORD = 'rhngiswryyybicyo'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGIN_URL = 'login'

LOGOUT_REDIRECT_URL = 'login'

LOGIN_REDIRECT_URL = 'logout'

# local
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# Google

# GOOGLE_CLIENT_ID = '409261742060-bu1vn2j91081ed3l6aa0u4eplqvmglt2.apps.googleusercontent.com'
# SOCIAL_AUTH_PASSWORD = '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'

# server
# CHANNEL_LAYERS = {
#    "default": {
#        "BACKEND": "channels_redis.core.RedisChannelLayer",
#        "CONFIG": {
#            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
#        },
#    },
# }


# Authentication backends
AUTHENTICATION_CLASSES = (
    'dj_rest_auth.authentication.AllAuthJWTAuthentication',
)

# # Allauth settings
# SITE_ID = 1
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # or 'mandatory'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_LOGOUT_ON_GET = True

# Social account settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '954836385070-lgrgf01po3an5m8bihec7g6vibs0onit.apps.googleusercontent.com',
            'secret': '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',
        }
    },
    'github': {
        'APP': {
            'client_id': '86f2bfc0529d0ca764cc',
            'secret': 'bed949e6563f5acca103cba656115384845c9a2a',
        }
    },
    'facebook': {
        'APP': {
            'client_id': '863244545502688',
            'secret': '8d9a789122fc5f51ab48d03831412c45',
        }
    },
}
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'allauth.account.auth_backends.AuthenticationBackend',
    # ...
]
REST_USE_JWT = True
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'authentification.utils.jwt_response_payload_handler',
}

SIMPLE_JWT = {
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}
# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'SCOPE': ['email', 'public_profile'],
#         'METHOD': 'oauth2',
#         'VERIFIED_EMAIL': False,
#     },
# }
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '954836385070-lgrgf01po3an5m8bihec7g6vibs0onit.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GITHUB_KEY = '86f2bfc0529d0ca764cc'
SOCIAL_AUTH_GITHUB_SECRET = 'bed949e6563f5acca103cba656115384845c9a2a'

SOCIAL_AUTH_FACEBOOK_KEY = '863244545502688'
SOCIAL_AUTH_FACEBOOK_SECRET = '8d9a789122fc5f51ab48d03831412c45'
SOCIAL_AUTH_FACEBOOK_APP_NAME = 'facebook' 

FORCE_SCRIPT_NAME = '/v1'