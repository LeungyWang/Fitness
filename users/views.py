from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from . import models
from django.contrib import messages
# Create your views here.

def user_regist(request):
	return HttpResponse("Hello World")

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get("password")
		if username and password :
			try:
				user = models.New_User.objects.get(vip_name=username)
			except:
				messages.error(request, '用户不存在！')
				return render(request, 'users/login.html')
			if user.vip_password == password:
				messages.error(request, '登陆成功！')
				return render(request,'users/index.html')
			else:
				messages.error(request, '密码错误！')
	return render(request,'users/login.html')

def user_main(request):
	return render(request,'users/index.html')
