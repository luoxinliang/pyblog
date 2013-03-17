#!/usr/bin/env python
#coding=utf-8
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/check_weibo_auth/$', 'blog.admin_views.check_weibo_auth'),
    url(r'^admin/weibo/auth/$', 'blog.admin_views.admin_weibo_auth'),
    url(r'^admin/weibo/auth/done/$', 'blog.admin_views.admin_weibo_auth_deal'),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/', include('social.urls')),
    url(r'^', include('blog.urls')),

#    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/cheng/workspace/bjiang/tpl/img/css'}),
#    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/cheng/workspace/bjiang/tpl/img/js'}),
#    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/cheng/workspace/bjiang/tpl/img/images'}),

)

# Static files url if DEBUG
urlpatterns += staticfiles_urlpatterns()

#urlpatterns = patterns('',
#    # Uncomment the next line to enable the admin:
#    url(r'^admin/check_weibo_auth/$', 'blog.admin_views.check_weibo_auth'),
#    url(r'^admin/weibo/auth/$', 'blog.admin_views.admin_weibo_auth'),
#    url(r'^admin/weibo/auth/done/$', 'blog.admin_views.admin_weibo_auth_deal'),
#    url(r'^admin/', include(admin.site.urls)),
#)

# Grappelli url mapping
#urlpatterns += patterns('',
#    (r'^grappelli/', include('grappelli.urls')),
#    (r'^admin/filebrowser/', include(site.urls)),
#)

## Accounts
#urlpatterns += patterns('',
#    (r'^accounts/', include('social.urls'))
#)
#    
## Blog
#urlpatterns += patterns('',
#    (r'^', include('blog.urls'))
#)

