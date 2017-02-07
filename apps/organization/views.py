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
        all_orgs = CourseOrg.objects.all()      # 课程机构
        org_nums = all_orgs.count()
        all_citys = City.objects.all()          # 城市
        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(all_orgs, 4, request=request)         # 5 表示每页显示的条数为 5

        orgs = p.page(page)

        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
        })



