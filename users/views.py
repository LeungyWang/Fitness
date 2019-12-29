from django.shortcuts import render,redirect
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
		usertype = request.POST.get("usertype")
		if username and password :
			if usertype is "0":
				try:
					user = models.User_Login.objects.get(user_name=username)
				except:
					messages.error(request, '用户不存在！')
					return redirect("/account/index")
				if user.user_password == password:
					request.session['is_login']=True
					request.session['user_name']=username
					return render(request,'users/index.html')
				else:
					messages.error(request, '密码错误！')
					return redirect("/account/index")
			elif usertype is "1":
				try:
					user = models.Admin_Login.objects.get(admin_name=username)
				except:
					messages.error(request, '用户不存在！')
					return redirect("/account/index")
				if user.admin_password != password:
					messages.error(request, '密码错误！')
					return redirect("/account/index/")
				else:
					request.session['is_login'] = True
					request.session['user_name'] = username
					return render(request,'users/index.html')
			else:
				raise Exception
	return render(request,'users/login.html')
