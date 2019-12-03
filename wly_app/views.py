from django.shortcuts import render,redirect
from .form import BodyCheckForm
from .models import BodyData
from . import models
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
# Create your views here.

def body_check(request):
    username = request.session.get("user_name")
    if request.method == "POST":
        form = BodyCheckForm(request.POST)
        if form.is_valid():
            hight = form.cleaned_data["hight"]
            heigth = form.cleaned_data["height"]
            chest = form.cleaned_data["chest"]
            waist = form.cleaned_data["waist"]
            hip = form.cleaned_data["hip"]
            queith = form.cleaned_data["queith"]
            maxh = form.cleaned_data["maxh"]
            try :
                BodyData.objects.get.get(user_name=username)
                bd = BodyData.objects.get(user_name=username)
                bd.hight = hight
                #form.fields['hight'].value= hight
                bd.height = heigth
                bd.chest = chest
                bd.waist = waist
                bd.hip = hip
                bd.queith = queith
                bd.maxh = maxh
                bd.save()
            except:
                bd = BodyData(user_name=username, hight=hight, height=heigth, chest=chest, waist=waist, hip=hip,
                              queith=queith, maxh=maxh)
                bd.save()
            messages.success(request,"保存成功")
            return render(request, "wly_app/body.html", locals())
        else:
            error_msg =form.errors
            return render(request,"wly_app/body.html",{'form':form,"errors":error_msg})
    try:
        BodyData.objects.get(user_name=username)
        flag = True
        bd = models.BodyData.objects.get(user_name=username)
        hight = bd.hight
        height = bd.height
        chest = bd.chest
        waist = bd.waist
        hip = bd.hip
        queith = bd.queith
        maxh = bd.maxh
        return render(request, "wly_app/body.html", locals())
    except:
        flag = False

    return render(request,"wly_app/body.html",{'form':BodyCheckForm})
