# Django settings for testsite project.
# -*- coding: utf-8 -*- 

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#SITE_URL = "http://localhost:8080"

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = 'bjiang'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'postgres'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'luocheng'         # Not used with sqlite3.
#DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = '5432'             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%n#0$r_d^og!u-i_p2@u*4py)4wkxleq#^q2!91c7&5)kvtw*2'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
#    'django.template.loaders.eggs.load_template_source',
    
#    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.filesystem.Loader',    
#    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
#    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'account.middleware.AuthenticationMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath("tpl"),
)

INSTALLED_APPS = (
#    'django.contrib.auth',
    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'django.contrib.sitemaps',
    'account',
    "blog",
    "social",
    'qqweibo',
)

#SESSION_ENGINE = 'django.contrib.sessions.backends.db'
#SESSION_ENGINE = 'django.contrib.sessions.backends.redis_session'
#SESSION_ENGINE = 'redis_sessions.session'

#SESSION_REDIS_HOST = 'localhost'
#SESSION_REDIS_PORT = 6379
#SESSION_REDIS_DB = 0
#SESSION_REDIS_PASSWORD = ''
#SESSION_REDIS_PREFIX = 'session'

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

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'bjiang',
#        'USER': 'postgres',
#        'PASSWORD': 'luocheng',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'console':{
#            'level':'DEBUG',
#            'class':'logging.StreamHandler',
#        },
#    },
#    'loggers': {
#        'django.db.backends': {
#            'handlers': ['console'],
#            'propagate': True,
#            'level':'DEBUG',
#        },
#    }
#}

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
