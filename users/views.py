from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from . import models
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
				return render(request, 'users/login.html')
			if user.vip_password == password:
				return render(request,'users/index.html')
	return render(request,'users/login.html')

def user_main(request):
	return render(request,'users/index.html')