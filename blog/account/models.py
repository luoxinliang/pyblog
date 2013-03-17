#coding=utf-8

from account.signals import user_logged_in
from base.util import get_client_ip
from django.contrib.auth.hashers import check_password
from django.db import models
from django.utils.translation import ugettext_lazy as _
from string import join
import datetime
import time

def update_last_login(sender,request,user,**kwargs):
    user.last_login_time = time.time()
    user.login_times += 1
    user.last_login_ip = get_client_ip(request)
    user.is_active = True
    user.save()
user_logged_in.connect(update_last_login)

class User(models.Model):
#    GENDER_CHOICES = (
#        ('M', 'Male'),
#        ('F', 'Female'),
#    )
#    username = models.CharField(max_length=30, unique=True,
#        help_text=_('字母、数字或下划线组成，长度小于30个字符'),blank=True)
#    id = models.AutoField(default=1000000,primary_key=True)   ALTER TABLE table_name AUTO_INCREMENT=1000000
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    pp = models.CharField(max_length=40,blank=True,null=True)
    
    regist_ip = models.IPAddressField(blank=True,null=True)
    regist_time = models.DateTimeField(default=datetime.datetime.now())
    invite_uid = models.IntegerField(default=0)
    login_times = models.IntegerField(default=1)
    last_login_time = models.DateTimeField(default=datetime.datetime.now())
    last_login_ip = models.IPAddressField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    qq = models.CharField(max_length=13,blank=True)
    tel = models.CharField(max_length=20,blank=True)
    alipay = models.CharField(max_length=50,blank=True)
#    gender = models.CharField(max_length=30,choices=GENDER_CHOICES)
    
    invite_code = models.CharField(max_length=20,blank=True)                  # 邀请码
    invite_count = models.IntegerField(default=0)                             #共邀请人数
    invite_shop_count = models.IntegerField(default=0)                        #邀请人购物人数

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.email
    
    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            self.save()
        return check_password(raw_password, self.password, setter)
    
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
    
    @classmethod
    def get_user(cls,uid):
        try:
            return cls.objects.get(pk=uid)
        except:
            return None
        
    @classmethod
    def get_user_email(cls,email):
        try:
            return cls.objects.get(email=email)
        except:
            return None
    
    @classmethod
    def get_by_invite_code(cls,invite_code):
        try:
            return cls.objects.get(invite_code=invite_code)
        except:
            return None
        
    def gen_invite_code(self):
        ''' 生成邀请码 '''
        return hex(self.id+10000)
    
    @classmethod
    def get_list(cls,page=1,page_size=15):
        try:
            return User.objects.order_by('-id')[(page-1)*page_size:page*page_size]
        except Exception,e:
            return None
        
    @classmethod
    def get_count(cls):
        try:
            return cls.objects.all().count()
        except Exception,e:
            return 0
    
    def get_hide_email(self):
        email = self.email
        if email:
            start = email.find("@")
            if start<3:
                return email[:start] + "***" + email[start:len(email)]
            else:
                return email[:2] + "***" + email[start:len(email)]
        return ""
    
    def get_hide_tel(self):
        tel = self.tel
        if tel:
            return tel[:3] + "****" + tel[7:len(tel)]
        return ""
        
     
class AnonymousUser(object):
    uid = None
    username = ''
    is_staff = False

    def __init__(self):
        pass

    def __unicode__(self):
        return 'AnonymousUser'

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 1 # instances always return the same hash value

    def save(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def set_password(self, raw_password):
        raise NotImplementedError

    def check_password(self, raw_password):
        raise NotImplementedError

    def is_anonymous(self):
        return True

    def is_authenticated(self):
        return False

class Invite(models.Model):
    invite_user = models.ForeignKey("User",related_name="i_invite_user")   # 邀请人
    to_user = models.ForeignKey("User",related_name="i_to_user")           # 被邀请人
    join_time = models.DateTimeField(default=datetime.datetime.now())      # 产生时间
    
    @classmethod
    def get_invite_list(cls,invite_user,page=1,page_size=15):
        try:
            return cls.objects.filter(invite_user=invite_user)[(page-1)*page_size:page*page_size]
        except:
            return None
        
    @classmethod
    def get_invite_count(cls,invite_user):
        try:
            return cls.objects.filter(invite_user=invite_user).count()
        except:
            return 0
