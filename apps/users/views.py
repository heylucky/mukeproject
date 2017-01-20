# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate,login


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username", "")                # 值 ”默认是空
        pass_word = request.POST.get("password","")
        user = authenticate(username=user_name,password=pass_word)      # 形参是固定的不能修改

        if user is not None:
            login(request,user)                                         # 完成login登录,下面跳到首页
            return render(request,"index.html",{})
        else:
            return render(request,"login.html",{})
    elif request.method == 'GET':
        return render(request,'login.html',{})



