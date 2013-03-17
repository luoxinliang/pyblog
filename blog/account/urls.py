from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login$', 'account.views.login', name='user_login'),
    url(r'^regist$', 'account.views.regist', name='user_regist'),
    url(r'^logout','account.views.logout',name="user_logout"),
    url(r'^toinvite','account.views.toinvite',name="user_toinvite"),
    
    url(r'^valid/email','account.views.ajax_email_valid',name="user_ajax_email_valid"),
#    url(r'^home$', 'admin.views.home', name='admin_home'),
#    url(r'^share$', 'admin.views.share_check', name='share_check'),
#    url(r'^add_cate$', 'admin.views.add_category', name='add_cate'),
)