# _*_ coding:utf-8 _*_
__author__ = 'Jack Lin'

from django import forms
from operation.models import UserAsk

class UserAskForm(forms.Form):
    name = forms.CharField(required=True,max_length=20,min_length=2)
    mobile = forms.CharField(required=True,min_length=11,max_length=11)
    course_name = forms.CharField(required=True,max_length=10,min_length=10)
