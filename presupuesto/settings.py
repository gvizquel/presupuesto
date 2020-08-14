"""
Django settings for presupuesto project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Django Libraries
from django.utils.translation import gettext_lazy as _

# Thirdparty Libraries
import environ

ENVIROMENT = environ.Env()  # set default values and casting
environ.Env.read_env()  # reading .env file

SECRET_KEY = ENVIROMENT("SECRET_KEY")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = ENVIROMENT("DEBUG")

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "loe.terna.net", "admin.loe.terna.net"]


# Application definition

INSTALLED_APPS = [
    'apps.rosetta',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",
    'bootstrap4',
    'bootstrap_datepicker_plus',
    "usercustom",
    "main",
    "dominio",
    "producto",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "presupuesto.urls"

# ==================================================================================== #
"""Cada procesor de contexto de los templates tiene su razon de ser para mayor
detalle: https://docs.djangoproject.com/en/2.2/ref/templates/api/
"""
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # 'DIRS': [],
        # 'APP_DIRS': True,
        "OPTIONS": {
            "loaders": ["django.template.loaders.app_directories.Loader"],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.csrf",
            ],
        },
    },
]

WSGI_APPLICATION = "presupuesto.wsgi.application"


# #################################### EMAIL CONFIG ################################## #
EMAIL_BACKEND = ENVIROMENT("EMAIL_BACKEND")
EMAIL_HOST = ENVIROMENT("EMAIL_HOST")
EMAIL_PORT = ENVIROMENT("EMAIL_PORT")
EMAIL_HOST_USER = ENVIROMENT("EMAIL_USER")
EMAIL_HOST_PASSWORD = ENVIROMENT("EMAIL_PASSWORD")
EMAIL_USE_TLS = True


# ################################## Data Base CONFIG ################################ #
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": ENVIROMENT("DBUSER"),
        "NAME": ENVIROMENT("DBNAME"),
        "PASSWORD": ENVIROMENT("DBPASSWORD"),
        "HOST": ENVIROMENT("DBHOST"),
        "DATABASE_PORT": ENVIROMENT("DBPORT"),
    }
}

# ========================================================================== #
""" Esta configuración hace disponible todas esta variables en cualquier
plantilla
"""
PROJECT_NAME = 'Presupuesto Facil'
SLOGAN = 'Software de Gestión de Presupuestos'
PREFIX = 'Presupuesto'
SUFIX = 'Facil'
VERSION = '1.0'
INITIAL_A = 'P'
INITIAL_B = 'F'

SETTINGS_EXPORT = [
    'PROJECT_NAME',
    'SLOGAN',
    'PREFIX',
    'SUFIX',
    'VERSION',
    'INITIAL_A',
    'INITIAL_B'
]


# ==================================================================================== #
""" Esta configuración define el modelo personalizado para auth.user. Tambien
establece las rutas para algunas funciones.
"""
AUTH_USER_MODEL = "usercustom.UserCustom"
LOGIN_URL = "usercustom:login"
LOGOUT_REDIRECT_URL = "usercustom:login"
LOGIN_REDIRECT_URL = "usercustom:profile"


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ==================================================================================== #
""" Este bloque contiene toda la configuración para la loclización
"""
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# def gettext(cadena):
#     '''  "dummy" gettext() function
#     '''
#     return cadena

LANGUAGE_CODE = "en"
TIME_ZONE = "America/Caracas"
# Restricts languages
# Al usar lenguages del tipo en-us. es-ve, fr-ca no funciona la traducción
LANGUAGES = [("en", _("English")), ("es", _("Spanish")), ("fr", _("French"))]
# Where Django looks for translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ################################## rosetta Config ################################## #
ROSETTA_EXCLUDED_APPLICATIONS = (
    "dal_select2",
    "django_extensions",
    "mptt",
    "zinnia",
    "django_comments",
)

# #################################### Stic Config ################################### #
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = "media"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
