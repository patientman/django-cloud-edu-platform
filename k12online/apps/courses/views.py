# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course

# Create your views here.


class CourseListView(View):
	def get(self, request):
		all_courses = Course.objects.all().order_by("-add_time")

		hot_courses = Course.objects.all().order_by("-click_nums")[:3]

		# 课程排序
		sort = request.GET.get("sort", "") # get param: "?sort=param"
		if sort:
			if sort == "students":
				all_courses = all_courses.order_by("-student_nums")
			elif sort == "hot":
				all_courses = all_courses.order_by("-click_nums")

		# 分页
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1
		p = Paginator(all_courses, 9, request=request)
		courses = p.page(page)

		return render(request, 'course-list.html', {
			'all_courses':courses,
			'sort':sort,
			'hot_courses':hot_courses,
		})


class CourseDetailView(View):
	# 课程详情
	def get(self, request, course_id):
		course = Course.objects.get(id=int(course_id))

		# 点击数
		course.click_nums += 1
		course.save()

		return render(request, 'course-detail.html', {
			"course":course,
		})
