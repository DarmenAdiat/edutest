"""
Django settings for online_courses project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, LDAPSearchUnion
import ldap
from pathlib import Path
import os
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, LDAPSearchUnion

import os
import ldap
import logging
from pathlib import Path
from datetime import timedelta
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, LDAPSearchUnion
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)0a+fbjaf599ig=nz3=hd3xkm9y7y1^up70b351z-+q22-b8&g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ['http://192.168.129.44:6540', 'https://audittest.finreg.kz']
SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
CSRF_COOKIE_SECURE = False     # Set to True if using HTTPS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',

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

ROOT_URLCONF = 'online_courses.urls'

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

WSGI_APPLICATION = 'online_courses.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join('courses', 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'courses.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/image')

STATIC_ROOT = BASE_DIR / "staticfiles"



AUTH_LDAP_SERVER_URI = "ldap://finreg.rk:389"
AUTH_LDAP_BIND_DN = r"FINREG\UNT_websrep"
AUTH_LDAP_BIND_PASSWORD = "Friday2025!"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "OU=Almaty, DC=finreg, DC=rk",
    ldap.SCOPE_SUBTREE,
    "(&(objectClass=user)(sAMAccountName=%(user)s))"
)

AUTH_LDAP_DOMAIN_PREFIX = ''
# AUTH_LDAP_PROFILE_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     "title": "title",
#     "department": "department"
# }
AUTH_PROFILE_MODULE = 'main.UserProfile'

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "title": "title",
    "department": "department",
    "telephone_number": "telephoneNumber"
}
AUTH_USER_MODEL = 'courses.User'

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',  # Включите обычный бэкенд Django
)

CORS_ALLOWED_ORIGINS = [
    "https://edutest.finreg.kz",
]
CSRF_TRUSTED_ORIGINS = [
    'https://edutest.finreg.kz',
]