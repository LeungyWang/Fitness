from django.shortcuts import render,redirect
from .form import BodyCheckForm
from .models import BodyData
from . import models
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
# Create your views here.

def body_check(request):
    if request.method == "POST":
        form = BodyCheckForm(request.POST)
        if form.is_valid():
            username = request.session.get("user_name")
            if username is None:
                raise Exception
            hight = form.cleaned_data["hight"]
            heigth = form.cleaned_data["height"]
            chest = form.cleaned_data["chest"]
            waist = form.cleaned_data["waist"]
            hip = form.cleaned_data["hip"]
            queith = form.cleaned_data["queith"]
            maxh = form.cleaned_data["maxh"]
            if BodyData.objects.get(user_name=username):
                bd = BodyData.objects.get(user_name=username)
                bd.hight = hight
                bd.height = heigth
                bd.chest = chest
                bd.waist = waist
                bd.hip = hip
                bd.queith = queith
                bd.maxh = maxh
                bd.save()
            else:
                bd = BodyData(user_name=username, hight=hight, height=heigth, chest=chest, waist=waist, hip=hip,
                              queith=queith, maxh=maxh)
                bd.save()
            messages.success(request,"保存成功")
        else:
            error_msg =form.errors
            return render(request,"wly_app/body.html",{'form':form,"errors":error_msg})

    return render(request,"wly_app/body.html",{'form':BodyCheckForm})
