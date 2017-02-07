# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name=u'城市名', max_length=100)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)
    des= models.CharField(verbose_name=u'描述', max_length=200)

    class Meta:
        verbose_name=u'城市'
        verbose_name_plural=verbose_name

    def __unicode__(self):          # 重载unicode方法
        return self.name


class CourseOrg(models.Model):
    name= models.CharField(verbose_name=u'机构名称', max_length=100)
    desc= models.TextField(verbose_name=u'机构描述')
    catagory = models.CharField(verbose_name=u'机构类别',default="pxjg",max_length= 20,choices= (("pxjg",u"培训机构"),("gx","高校"),("gr","个人")))
    click_nums= models.IntegerField(verbose_name=u'点击数', default=0)
    fav_nums = models.IntegerField(verbose_name=u'收藏数', default=0)
    image = models.ImageField(verbose_name=u'logo', upload_to="org/%Y/%m")      # 机构封面logo
    address = models.CharField(verbose_name=u'机构地址',max_length=150)
    city=models.ForeignKey(City,verbose_name=u'所在城市')

    class Meta:
        verbose_name=u'课程机构'
        verbose_name_plural = verbose_name

    def __unicode__(self):          # 重载unicode方法
        return self.name

class Teacher(models.Model):
    name=models.CharField(verbose_name=u'机构名称',max_length=100)
    work_years=models.IntegerField(u'工作年限',default=0)
    work_company=models.CharField(verbose_name=u'就职公司',max_length=50)
    work_position=models.CharField(verbose_name=u'公司职位',max_length=50)
    point =models.CharField(verbose_name=u'教学特点', max_length=100)
    click_nums = models.IntegerField(u'点击数', default=0)
    fav_nums = models.IntegerField(u'收藏数', default=0)
    add_time=models.DateTimeField(u'添加时间', default=datetime.now)
    city = models.ForeignKey(City,verbose_name=u'所在城市')
    org = models.ForeignKey(CourseOrg, verbose_name=u'所在机构')

    class Meta:
        verbose_name=u'教师'
        verbose_name_plural = verbose_name