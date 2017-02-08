# _*_ coding:utf-8 _*_
__author__ = 'Jack Lin'

from django import forms
from operation.models import UserAsk        # 由数据库字段产生form字段



class UserAskForm(forms.ModelForm):
    # my_form = forms.CharField()       # 可以自定义forms
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']