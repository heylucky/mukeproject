# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg,City


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self,request):
        all_orgs = CourseOrg.objects.all()      # 机构
        hot_orgs = all_orgs.order_by("click_nums")[0:4]     # 按照点击次数排名，取出前4名
        all_citys = City.objects.all()          # 城市
        # 筛选城市
        city_id = request.GET.get('city',"")     # 取出从前端获得的城市
        if city_id:                             # 如果存在city_id
            all_orgs = all_orgs.filter(city_id=int(city_id))        # django 都可以对外键字段进行 XXX_id的形式

        # 类别筛选
        catagory = request.GET.get('ct','')     # 取出从前端获得的类别 ct= pxjg 、gx、gr
        if catagory:
            all_orgs = all_orgs.filter(catagory=catagory)

        sort = request.GET.get('sort')         # 取出从前端获得的学习人数或课程数 students or courses
        if sort:
            if sort =='students':
                all_orgs = all_orgs.order_by("-students")       # “-”表示倒序
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(all_orgs, 4, request=request)         # 5 表示每页显示的条数为 5
        orgs = p.page(page)
        org_nums = all_orgs.count()     # 进行计数

        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id': city_id,
            'catagory':catagory,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })



