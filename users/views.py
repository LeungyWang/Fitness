from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user_regist(requset):
	return HttpResponse("Hello World")



def user_login(requset):
	return render(requset,'users/login.html')

def user_main(requset):
	return render(requset,'users/index.html')