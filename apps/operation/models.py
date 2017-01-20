# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


class UserAsk(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=20)
    mobile = models.CharField(verbose_name=u'手机', max_length=11)
    course_name = models.CharField(verbose_name=u'课程名', max_length=50)
    add_time = models.DateTimeField(verbose_name=u'添加时间',default=datetime.now)

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural=verbose_name


class CourseComments(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name=u'用户')
    course=models.ForeignKey(Course,verbose_name=u'所评课程')
    comment=models.CharField(verbose_name=u'评论：', max_length=200)
    add_time = models.DateTimeField(verbose_name=u'添加时间',default=datetime.now)

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural=verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u'用户')
    fav_id=models.IntegerField(verbose_name=u'标志ID', default=0)#标志收藏的类型：课程，老师，机构
    fav_type=models.IntegerField(verbose_name=u'收藏类型', choices=((1, '课程'),(2,'课程机构'),(3,'讲师')),default=1)
    add_time= models.DateTimeField(verbose_name=u'收藏时间', default=datetime.now)

    class Meta:
        verbose_name = u'用户的收藏'
        verbose_name_plural=verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(verbose_name=u'接收用户',default=0)      # 用户接收的消息，用户可能是一个或多个，
                                                                         # 要给这些用户定向发送消息，因此用integer存放存放要发送的用户ID
    message = models.CharField(verbose_name=u'消息内容', max_length=500)
    has_read = models.BooleanField(verbose_name=u'是否已读', default=False)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural=verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'用户的课程'
        verbose_name_plural=verbose_name
