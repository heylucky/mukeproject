# _*_ coding:utf-8 _*_
__author__ = 'Jack Lin'


import xadmin
from xadmin import views

from models import UserProfile,EmailVerifyRecord,Banner


class BaseSetting(object):
    enable_themes=True      #使能主题功能
    use_bootswatch = True       #使用多种样式可选


class GlobalSetting(object):
    site_title="后花园系统"
    site_footer="林越林"
    menu_style="accordion"


class EmailVerifyRecordAdmin(object):
    list_display=['code','email','send_type','send_time']
    search_fields =['code','email','send_type']


class UserProfileAdmin(object):
    list_display=['nick_name','gender','address','mobile']
    search_fields =['nick_name','gender','address','mobile']
    list_filter =['nick_name','gender','address','mobile']


class BannerAdmin(object):
    list_display=['title','image','url','index','add_time']
    search_fields =['title','image','url','index']


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Banner,BannerAdmin)