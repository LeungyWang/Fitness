from django.shortcuts import render
from django.http import JsonResponse
from ly_app.models import *
from users.models import New_User,User_Login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def ly_test(request):
	# 获取用户数据
	course_list = course.objects.all()

	return render(request,'ly_app/course.html',{"course_list":course_list})
def ly_coach(request):
	coach_list = coach.objects.all()
	return render(request,'ly_app/coach.html',{"coach_list":coach_list})
def ly_info(request):
	username = request.session.get('user_name')
	try:
		info_list = New_User.objects.get(login_name = username)
	except:
		New_User(login_name_id=username).save()
		info_list = New_User.objects.get(login_name = username)
	result_course = info_list.courseById.all()
	print(result_course)
	result_coach = info_list.coachById.all()
	return render(request,'ly_app/info.html',locals())
@csrf_exempt
def ly_coach_in(request):
	if request.method=="POST":
		name=request.POST.get("name")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		sense=request.POST.get("sense")
		r = coach(name=name,sex=sex,age=age,sense=sense)
		r.save()
		return JsonResponse({"data":"success!"})
	else:
		return render(request,"ly_app/coachi_in.html")

@csrf_exempt
def ly_course_in(request):
	if request.method=="POST":
		name=request.POST.get("name")
		spendtime=request.POST.get("timelong")
		starttime=request.POST.get("times")
		classroom=request.POST.get("classroom")
		person=request.POST.get("person")
		r = course(name=name,spendtime=spendtime,starttime=starttime,classroom=classroom,person=person)
		r.save()
		return JsonResponse({"data":"success!"})
	else:
		return render(request,"ly_app/course_in.html")
@csrf_exempt
def course_choose(request):
	courseid=request.POST.get("courseid")
	username = request.session.get('user_name')
	info_list = New_User.objects.get(login_name=username)
	info_list.courseById.add(courseid)
	return JsonResponse({"data": "success!"})

@csrf_exempt
def course_del(request):
	courseid=request.POST.get("courseid")
	course.objects.filter(courseid=int(courseid)).delete()
	return JsonResponse({"data": "删除成功!"})

@csrf_exempt
def course_edit(request):
	courseid=request.POST.get("courseid")
	name = request.POST.get("name")
	spendtime = request.POST.get("timelong")
	starttime = request.POST.get("times")
	classroom = request.POST.get("classroom")
	person = request.POST.get("person")
	course.objects.filter(courseid=courseid).update(name=name, spendtime=spendtime, starttime=starttime, classroom=classroom, person=person)
	return JsonResponse({"data": "修改成功!"})
@csrf_exempt
def coach_choose(request):
	coachid=request.POST.get("coachid")
	username = request.session.get('user_name')
	info_list = New_User.objects.get(login_name=username)
	info_list.coachById.add(coachid)
	return JsonResponse({"data": "success!"})
@csrf_exempt
def save_info(request):
	username = request.session.get('user_name')
	name=request.POST.get("name")
	sex = request.POST.get("sex")
	bir = request.POST.get("bir")
	phone = request.POST.get("phone")
	email = request.POST.get("email")
	duration = request.POST.get("duration")
	level = request.POST.get("level")
	New_User.objects.filter(login_name=username).update(vip_name=name,vip_sex=sex,vip_birthday=bir,vip_phone=phone,vip_email=email,vip_duriation=duration,vip_level=level)
	return JsonResponse({"data": "success!"})
@csrf_exempt
def UserCourse_del(request):
	username = request.session.get('user_name')
	courseid = request.POST.get("courseid")
	info_list = New_User.objects.get(login_name=username)
	course_obj = course.objects.get(courseid=int(courseid))
	print(course)
	info_list.courseById.remove(course_obj)
	return JsonResponse({"data": "退选成功!"})
@csrf_exempt
def UserCoach_del(request):
	username = request.session.get('user_name')
	coachid = request.POST.get("coachid")
	info_list = New_User.objects.get(login_name=username)
	coach_obj = coach.objects.get(coachid=int(coachid))
	print(course)
	info_list.coachById.remove(coach_obj)
	return JsonResponse({"data": "退选成功!"})
@csrf_exempt
def coach_del(request):
	coachid=request.POST.get("coachid")
	coach.objects.filter(coachid=int(coachid)).delete()
	print("yes")
	return JsonResponse({"data":"删除成功"})
@csrf_exempt
def coach_edit(request):
	coachid = request.POST.get("coachid")
	name = request.POST.get("name")
	sex = request.POST.get("sex")
	age = request.POST.get("age")
	sense = request.POST.get("sense")
	coach.objects.filter(coachid=coachid).update(name=name,sex=sex,age=age,sense=sense,)
	return JsonResponse({"data":"修改成功！"})