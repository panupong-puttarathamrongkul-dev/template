"""
Django settings for template project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") or False

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'template',
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

ROOT_URLCONF = 'template.urls'

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

WSGI_APPLICATION = 'template.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# # Handle CORS when in debug mode.
# # See: https://github.com/ottoyiu/django-cors-headers
# if DEBUG:
#     MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware"] + MIDDLEWARE
#     INSTALLED_APPS += ["corsheaders"]
#     CORS_ORIGIN_ALLOW_ALL = True
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": "",
#             "USER": "",
#             "PASSWORD": "",
#             "HOST": "127.0.0.1",
#             "PORT": "5432",
#         }
#     }
#     TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
# else:
#     # Database
#     # https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#     DATABASES = {"default": dj_database_url.config(conn_max_age=500)}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = [
# os.path.join(BASE_DIR, 'static'),
# THS: "npm run build" will create files in the following
# locations. Not sure why need to add both locations, but
# collectstatic will fail otherwise.
# os.path.join(BASE_DIR, "build"),
# ]

# Whitenoise
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# Whitenoise
# See: https://github.com/evansd/whitenoise/blob/master/docs/django.rst
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# To test whether the problems are due to WhiteNoise or not, try swapping the
# WhiteNoise storage backend for the Django one:
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
