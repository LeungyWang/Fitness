from django.shortcuts import render
from . import models
from users import models
# Create your views here.
def ly_test(request):
	# 获取用户数据
	course_list = models.course.objects.all()

	return render(request,'ly_app/course.html',locals())
def ly_coach(request):
	return render(request,'ly_app/coach.html')
def ly_info(request):
	username = request.session.get('user_name')
	info_list = models.New_User.objects.get(login_name = username)
	return render(request,'ly_app/info.html',locals())