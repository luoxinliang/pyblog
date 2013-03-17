# -*- coding:Utf-8 -*-

from django import forms

class RegistForm(forms.Form):  
    email = forms.EmailField(label=(u"邮件"), max_length=30, widget=forms.TextInput(attrs={'size': 30,'class':'abc', }))      
    password = forms.CharField(label=(u"密码"), max_length=30, widget=forms.PasswordInput(attrs={'size': 20, }))  
    repassword = forms.CharField(label=(u"重复密码"), max_length=30, widget=forms.PasswordInput(attrs={'size': 20, }))  

#    username = forms.CharField(label=(u"昵称"), max_length=30, widget=forms.TextInput(attrs={'size': 20, }))  
      
#    def clean_username(self):  
#        '''''验证重复昵称'''  
#        users = User.objects.filter(username__iexact=self.cleaned_data["username"])  
#        if not users:  
#            return self.cleaned_data["username"]  
#        raise forms.ValidationError((u"该昵称已经被使用请使用其他的昵称"))  
          
#    def clean_email(self):  
#        '''验证重复email'''
#        email = self.cleaned_data["email"]
#        if email:
#            emails = UserRegist.objects.filter(email__iexact=email)  
#            if not emails:  
#                return self.cleaned_data["email"]  
#            raise forms.ValidationError((u"该邮箱已经被注册！"))
#        else:
#            raise forms.ValidationError((u"邮箱不能为空！")) 
        
#    def clean_password(self):
#        password = self.cleaned_data['password']
#        password2 =  self.cleaned_data['password2']
#        if(password == password2):
#            '''加密密码'''
#            return make_password()
#        else:
#            raise forms.ValidationError((u"两次密码输入不一致！"))   
    
class LoginForm(forms.Form):  
    email = forms.CharField(label=(u"昵称"), max_length=30, widget=forms.TextInput(attrs={'size': 20, }))  
    password = forms.CharField(label=(u"密码"), max_length=30, widget=forms.PasswordInput(attrs={'size': 20, }))  

class AjaxEmailValidForm(forms.Form):  
    email = forms.CharField(label=(u"email"), max_length=30, widget=forms.TextInput(attrs={'size': 20, }))  
  