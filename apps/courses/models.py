# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(u'课程名',max_length=100)
    desc=models.CharField(u'课程描述',max_length=100,default='无')
    detail=models.TextField(u'课程详情',default='无')
    degree=models.CharField(u'难度',choices=(('cj','初级'),('zj','中级'),('gj','高级')),max_length=10)
    learn_time=models.IntegerField(u'学习时长(min)', default=0)
    students_nums=models.IntegerField(u'学习人数', default=0)    # 点击“我要学习”
    fav_nums=models.IntegerField(u'收藏人数', default=0)
    image=models.ImageField(u'封面', upload_to='course/%Y/%m',max_length=100,blank=True)
    click_nums = models.IntegerField(u'点击数', default =0 )
    add_time=models.DateTimeField(u'添加时间',default=datetime.now)

    class Meta:
        verbose_name=u'课程名称'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name=u'课程')
    name=models.CharField(u'章节名称',max_length=100, blank=True)
    add_time=models.DateTimeField(u'添加时间',default=datetime.now)

    class Meta:
        verbose_name=u'章节名称'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name=u'章节')
    name=models.CharField(u'视频名',max_length=50)
    add_time=models.DateTimeField(u'添加时间',default=datetime.now)

    class Meta:
        verbose_name=u'视频名称'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name


class CourseResourse(models.Model):
    course=models.ForeignKey(Course,verbose_name=u'课程')
    name=models.CharField(u'资源名',max_length=100)
    download=models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u'资源文件',max_length=100)
    add_time=models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name=u'课程资源'
        verbose_name_plural=verbose_name