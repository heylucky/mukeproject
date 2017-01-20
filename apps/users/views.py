# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))        #用户名或邮件登录
            if user.check_password(password):       # 检查明文暗纹密码是否一样
                return user
        except Exception as e:
            return None

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username", "")                # 值 ”默认是空
        pass_word = request.POST.get("password","")
        user = authenticate(username=user_name,password=pass_word)      # 形参是固定的不能修改

        if user is not None:
            login(request,user)                                         # 完成login登录,下面跳到首页
            return render(request,"index.html",{})
        else:
            return render(request,"login.html",{'msg': '用户名或密码错误！'})
    elif request.method == 'GET':
        return render(request,'login.html',{})



