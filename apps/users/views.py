# _*_ coding:utf-8 _*_
from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login,logout       # 权限认证 ，登录，退出
from django.contrib.auth.backends import ModelBackend           # 自定义后台auth认证的方法，邮箱、用户名或者手机号登录
from django.db.models import Q                                  # 登录方式的选择
from django.views.generic.base import View                      # 视图
from django.contrib.auth.hashers import make_password       # 对明文密码进行加密

from .models import UserProfile, EmailVerifyRecord
from forms import LoginForm,RegisterForm,ForgetForm,ModifyPwdForm
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):                  # settings.py中的元组 ：AUTHENTICATION_BACKENDS
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))        # 用户名或邮件登录(后续可以添加手机登录)
            if user.check_password(password):       # 检查 明文-暗文 密码是否一样:True or False,此为AbstractUser的方法
                return user
        except Exception as e:
            return None


# 基于类的视图函数
class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():       # 实际是检查_errors是否为空，为空说明正常
            user_name = request.POST.get("username", "")  # 值“”默认是空
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)  # 形参是固定的不能修改
            if user is not None:
                if user.is_active:
                    login(request, user)  # 完成login登录,下面跳到首页
                    return render(request, "index.html", {})   # 跳到首页
                else:
                    return render(request,"login.html",{"msg":"用户未激活"})
            else:
                # if user.is_active:
                #     return render(request,"login.html",{"msg":"用户名或密码出错"})
                # else:
                return render(request,"login.html",{"msg":"用户名或密码出错"})
        else:
            return render(request, "login.html",{"login_form" : login_form})


class LogoutView(View):
    def get(self,request):
        pass

# 基于函数的视图,不推荐
# def user_login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get("username", "")                # 值 ”默认是空
#         pass_word = request.POST.get("password","")
#         user = authenticate(username=user_name,password=pass_word)      # 形参是固定的不能修改
#
#         if user is not None:
#             login(request,user)                                         # 完成login登录,下面跳到首页
#             return render(request,"index.html",{})
#         else:
#             return render(request,"login.html",{'msg': '用户名或密码错误！'})
#     elif request.method == 'GET':
#         return render(request,'login.html',{})


# 打开邮件的链接，进入该视图函数，is_active置为True，在loginView中判断是否激活，激活才可以登录
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code = active_code)
        # if EmailVerifyRecord.objects.get(code=active_code):
        if all_records :
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request,"login.html")
        else:
            return HttpResponse(content="<h1>连接失效</h1>")


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, "register.html",{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")  # 值“”默认是空,此时获取的user_name为邮箱地址
            if UserProfile.objects.filter(email=user_name):
                return render(request,"register.html",{"register_form": register_form,"msg":"用户已存在!!!"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name       # user_name 默认为邮箱
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()             # 保存到数据库当中。

            send_register_email(user_name,"register")
            return render(request,"login.html")
        else:
            return render(request,"register.html",{"register_form":register_form})  # 见html中register_form.errors.email/password; register_form.errors.items


class ForgetPwdView(View):
    def get(self,request):
        forget_form = ForgetForm()
        return render(request,"forgetpwd.html",{"forget_form":forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email","")
            send_register_email(email, "forget")
            return render(request,"send_success.html")
            # if UserProfile.objects.get(email=email):        # 如果提交的邮箱地址在数据库中存在
            #     pass
        else:
            return render(request,"forgetpwd.html",{"msg":u"不存在此邮箱"})


class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code = reset_code)
        # if EmailVerifyRecord.objects.get(code=active_code):
        if all_records :
            for record in all_records:
                email = record.email
                return render(request,"password_reset.html",{"email": email})
        else:
            return HttpResponse(content="<h1>重置密码连接失效</h1>")
        return render(request,"login.html")


class ModifyView(View):
    def post(self,request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1","")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email","")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email},{"msg":u"密码不一致"})
            user = UserProfile.objects.get(email = email)
            user.password = make_password(pwd2)
            user.save()
            return render(request,"login.html",{})
        else:
            email = request.POST.get("email","")
            return render(request, "password_reset.html",{"email":email,"modify_form":modify_form })

