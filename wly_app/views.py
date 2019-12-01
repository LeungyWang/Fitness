from django.shortcuts import render,redirect
from .form import BodyCheckForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from . import models
from django.contrib import messages
# Create your views here.

def body_check(request):
    if request.method == "POST":
        form = BodyCheckForm(request.POST)
        if form.is_valid():
            hight = form.cleaned_data["hight"]
            hegith = form.cleaned_data["height"]
            chest = form.cleaned_data["chest"]
            waist = form.cleaned_data["waist"]
            hip = form.cleaned_data["hip"]
            queith = form.cleaned_data["queith"]
            maxh = form.cleaned_data["maxh"]
            return JsonResponse(form.clean_data)
        else:
            errors_msg = form.errors
            return render(request, "wly_app/body.html", {'form': BodyCheckForm, 'errors': errors_msg})
    return render(request,"wly_app/body.html",{'form':BodyCheckForm})