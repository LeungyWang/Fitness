from django.shortcuts import render
from . import models
# Create your views here.
def ly_test(request):
	# 获取用户数据
	course_list = models.course.objects.all()

	return render(request,'ly_app/test.html',locals())
