# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name=models.CharField(verbose_name='昵称',max_length=20)
    birthday=models.CharField(verbose_name='生日',max_length=10,null=True)
    gender=models.CharField(verbose_name='性别',choices=(('male','男性'),('female','女性')),max_length=6,default='male')
    address=models.CharField(verbose_name=u'地址',max_length=100,null=True)
    mobile=models.CharField(verbose_name=u'联系方式',max_length=11,null=True)
    image=models.ImageField(verbose_name=u'头像',max_length=100,upload_to='image/%Y/%m',default=u'image/default.png')

    class Meta:
        verbose_name=u'用户信息'
        verbose_name_plural= '用户信息s'

    def __unicode__(self):
        return self.nick_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name=u'验证码',max_length=20)
    email = models.CharField(verbose_name=u'邮箱',max_length=30)
    send_type= models.CharField(verbose_name='发送类型',choices=(('register','注册'),('forget','找回密码')),max_length=30)
    send_time = models.DateTimeField(verbose_name=u'发送时间',default=datetime.now)  #这里datetime.now()要把括号去掉，不然是这个时间是调用这个model编译的时间，而不是实例化时间

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name        #复数形式，否则是  邮箱验证码哈哈s

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title=models.CharField(verbose_name=u'标题',max_length=100,null=True)#显示名称
    image=models.ImageField(upload_to='banner/Y/%m',null=True,verbose_name=u'轮播图')
    url=models.URLField(verbose_name=u'轮播访问地址',null=True,max_length=200)
    index=models.IntegerField(verbose_name=u'图片顺序',default=100)#轮播图显示的顺序
    add_time = models.DateTimeField(verbose_name=u'添加时间',default=datetime.now)

    class Meta:
        verbose_name=u'主页轮播图'
        verbose_name_plural=verbose_name