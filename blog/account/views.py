#coding=utf-8

from account import login as auth_login, logout as auth_logout, authenticate
from account.forms import RegistForm, LoginForm, AjaxEmailValidForm
from account.models import User
from base.util import get_client_ip
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts.render import render_response
from my.models import Fortune


SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
REDIRECT_FIELD_NAME = 'next'

def regist(request,template_name='user.regist.tpl'):
    next_url = request.GET.get("next")
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if _email_not_exists(email):
                pwd = form.cleaned_data['password']
                repwd = form.cleaned_data['repassword']
                if pwd != repwd:
                    form.errors['msg'] = u"两次密码不一致！"
                else:
                    ip = get_client_ip(request)
                    user = User.objects.create()
                    user.email = email
                    password = make_password(pwd)
                    user.password = password
                    user.regist_ip = ip
                    user.last_login_ip = ip
                    try:
                        user.save()
                        fortune = Fortune(user=user,total=10,active_point=10,left=10)
                        fortune.save()
                    except Exception,e:
                        form.errors['msg'] = u"注册失败，请重试"
                    else:
                        if request.user.is_authenticated():
                            logout(request)
                        user = authenticate(email=email,password=pwd)
                        auth_login(request,user)
                        if next_url:
                            return redirect(next_url)
                        return redirect("/")
            else:
                form.errors['msg'] = u"email已经被注册啦！"
        else:
            form.errors['msg'] = u"输入信息不合法，请重试"
    else:
        form = RegistForm()
    return render_response(template_name,form=form,request=request,next_url=next_url)

#@sensitive_post_parameters()
#@csrf_protect
#@never_cache
def login(request,template_name='user.login.tpl'):
    next_url = request.GET.get("next")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            user = authenticate(email=email,password=pwd)
            if user is not None:
                auth_login(request,user)
                if next_url:
                    return redirect(next_url)
                return redirect("/")
            else:
                form.errors['msg'] = u"登录失败，请检查用户名和密码是否正确"
        else:
            form.errors['msg'] = u"输入信息格式不合法，请重试"
    else:
        form = LoginForm()
    return render_response(template_name,form=form,request=request,next_url=next_url)

def logout(request):
    next_url = request.GET.get('next')
    auth_logout(request)
    if next_url:
        return redirect(next_url)
    return redirect("/")    
 
@login_required
def toinvite(request,template="user.toinvite.tpl"):
    user = request.user
    return render_response(template,request=request,user=user)

def ajax_email_valid(request):
    if request.method == "POST":
        form = AjaxEmailValidForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            json = '{"result":"error","message":"该邮箱已被注册，请重新换一个"}'
            if _email_not_exists(email):
                json = '{"result":"ok","message":"该邮箱可以注册"}'
            return HttpResponse(json)

def _email_not_exists(email):
    ''' email 是否已经注册 没有返回 True '''
    try:
        user = User.objects.get(email=email)
    except:
        return True
    else:
        if user is not None:
            return False
    return False
