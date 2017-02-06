# _*_ coding:utf-8 _*_
__author__ = 'Jack Lin'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)       # required 表示必填字段
    password = forms.CharField(required=True,min_length=4)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=4)
    captcha = CaptchaField(error_messages={"invalid":u"lin验证码错误!!!"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u"lin验证码错误!!!"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True,min_length=4)
    password2 = forms.CharField(required=True,min_length=4)