import os
import dj_database_url
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", 'django-insecure-z!-(87j_p9c!ua)c90@ybn$w#iqj3xv6_y%(4w6jkj6&)cdf-(')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "RENDER" not in os.environ

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost"]

RENDER_EXTERNAL_HOSTNAME = os.getenv('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dental.urls'

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

WSGI_APPLICATION = 'dental.wsgi.application'

CORS_ALLOW_ALL_ORIGINS = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

USE_NO_DB = True
USE_LOCAL_DB = False

if USE_NO_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
    if DEBUG and USE_LOCAL_DB:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": str(os.getenv('DB_NAME_LOCAL2')),
                "USER": str(os.getenv('DB_USER_LOCAL2')),
                "PASSWORD": str(os.getenv('DB_PWD_LOCAL2')),
                "HOST": str(os.getenv('DB_HOST_LOCAL2')),
                "PORT": str(os.getenv('DB_PORT_LOCAL2')),
            }
        }
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": str(os.getenv('DB_NAME_EXTERN2')),
                "USER": str(os.getenv('DB_USER_EXTERN2')),
                "PASSWORD": str(os.getenv('DB_PWD_EXTERN2')),
                "HOST": str(os.getenv('DB_HOST_EXTERN2')),
                "PORT": str(os.getenv('DB_PORT_EXTERN2')),
            }
        }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

EMAIL_HOST = os.getenv('EMAIL_HOST_VAL', 'None')
EMAIL_HOST_USER = os.getenv('EMAIL_HST_USR_VAL', 'None')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PWD_VAL', 'None')
EMAIL_PORT = os.getenv('EMAIL_PORT_VAL', 'None')
EMAIL_TIMEOUT = 30
