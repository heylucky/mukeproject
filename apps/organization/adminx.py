# _*_ coding:utf-8 _*_
__author__ = 'Jack Lin'

import xadmin
from models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['name', 'des', 'add_time']
    search_fields = ['name', 'des']
    list_filter = ['name', 'des', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc','click_nums','fav_nums','image','address','city']
    search_fields = ['name', 'desc','click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc','click_nums','fav_nums','image','address','city']


class TeacherAdmin(object):
    list_display = ['name', 'work_company','work_years','work_position','click_nums','fav_nums','city','add_time']
    search_fields = ['name', 'work_company','work_years','work_position','click_nums','fav_nums','city']
    list_filter = ['name', 'work_company','work_years','work_position','click_nums','fav_nums','city','add_time']


xadmin.site.register(City,CityAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)