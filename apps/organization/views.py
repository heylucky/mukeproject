# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View


from .models import CourseOrg,City


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self,request):
        all_orgs = CourseOrg.objects.all()      # 课程机构
        org_nums = all_orgs.count()
        all_citys = City.objects.all()          # 城市
        return render(request,'org-list.html',{
            'all_orgs':all_orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
        })



