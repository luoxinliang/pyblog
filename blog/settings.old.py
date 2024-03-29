#!/usr/bin/env python
#coding=utf-8
# Django settings for ChineBlog project.

import os

from utils import get_path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('luoluo', 'luoxinliang.zh@gmail.com'),
)

MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': get_path(('db', 'chine.db')),                      # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'luocheng',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = get_path(('static', 'uploads')) if not DEBUG else get_path(('blog', 'static', 'uploads'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/static/uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = get_path('static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    get_path('root_static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j*c*g$p3s)!!_ec-=+uiaa)a^iy(=kb60x=!g5^pq(l1ali0#6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'ChineBlog.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    get_path('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'django.contrib.sitemaps',
    # Grapplli
#    'grappelli.dashboard',
#    'grappelli',
    # Filebrowser
#    'filebrowser',
    # mptt
#    'mptt',
    # Uncomment the next line to enable the admin:
#    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
#    'south',
    # blog, social
    'blog',
    'social',
    'qqweibo'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Self define
BLOG_THEME = 'coolblue'
# Needed install: PIL
# Grappelli
GRAPPELLI_ADMIN_TITLE = "残阳似血的博客"
GRAPPELLI_INDEX_DASHBOARD = 'ChineBlog.dashboard.CustomIndexDashboard'
# Filebrowser
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_VERSIONS = {
    'small_thumbnail': {'verbose_name': 'Small Thumbnail', 'width': 42, 'height': 42, 'opts': 'crop'},
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
}
FILEBROWSER_ADMIN_VERSIONS = ['small_thumbnail', 'thumbnail','small', 'medium']

SITE = 'http://127.0.0.1:8000' if DEBUG else 'http://qinxuye.me'
#SITE = 'http://qinxuye.me'
# Google authorized api
ENABLE_GOOGLE_ACCOUNT = False
GOOGLE_API = {
    'client_id': '',
    'client_secret': '',
    'redirect_urls': '',
    'refresh_token': '',
}
GOOGLE_AUTH_ENDPOINT = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_ACCESS_TOKEN_ENDPOINT = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_USERINFO_ENDPOINT = 'https://www.googleapis.com/oauth2/v1/userinfo'
GOOGLE_REDIRECT_URI = '%s/accounts/google/login/done/' % SITE

GOOGLE_SIMPLE_API_KEY = ''
# Google CustomSearch api
GOOGLE_SEARCH_ENGINE_UNIQUE_ID = ''
GOOGLE_CUSTOM_SEARCH_ENDPOINT = 'https://www.googleapis.com/customsearch/v1'
# Google Url Shortener api
GOOGLE_URL_SHORTENER_ENDPOINT = 'https://www.googleapis.com/urlshortener/v1/url'
                        
# Weibo
ENABLE_WEIBO_ACCOUNT = False
WEIBO_API = {
    'app_key': '',
    'app_secret': '',
    'redirect_urls': '',
}
WEIBO_AUTH_ENDPOINT = 'https://api.weibo.com/oauth2/authorize'
WEIBO_ACCESS_TOKEN_ENDPOINT = 'https://api.weibo.com/oauth2/access_token'
WEIBO_REDIRECT_URI = '%s/accounts/weibo/login/done/' % SITE
WEIBO_OAUTH_VERSION = 2
WEIBO_API_ENDPOINT = 'https://api.weibo.com/%d/' % WEIBO_OAUTH_VERSION

# Renren
ENABLE_RENREN_ACCOUNT = False
RENREN_API = {
    'api_key': '',
    'secret_key': '',
    'redirect_urls': '',
    'refresh_token': '' # use to sync data when a post is created or else
}
RENREN_AUTH_ENDPOINT = 'https://graph.renren.com/oauth/authorize'
RENREN_ACCESS_TOKEN_ENDPOINT = 'https://graph.renren.com/oauth/token'
RENREN_REDIRECT_URI = '%s/accounts/renren/login/done/' % SITE
RENREN_API_ENDPOINT = 'http://api.renren.com/restserver.do'

# QQWeibo
ENABLE_QQWEIBO_ACCOUNT = False
QQWEIBO_API = {
    'app_key': '',
    'app_secret': '',
    'redirect_urls': '',
    'access_token_key': '', # use for oauth1 to sync data when a post is created or else
    'access_token_secret': '' # use for oauth1 to sync data when a post is created or else
}
QQWEIBO_REDIRECT_URI = '%s/accounts/qqweibo/login/done/' % SITE


# Email
ENABLE_EMAIL = False

# Comment must contans Chinese
ENABLE_COMMENT_CHN = False

#local settings
try:
    from local_settings import *
except ImportError:
    pass