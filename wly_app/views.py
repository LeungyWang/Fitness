from django.shortcuts import render,redirect
from .form import BodyCheckForm
from .models import BodyData
from .models import BodyParts
from users.models import New_User
from .models import BodytestStandard
from  .models import starlevel
from .models import GradeLevel
from .models import PartCourse
from .models import Courses
from . import models
from  .models import UserPysicalTest
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
from datetime import datetime
import matplotlib.pyplot as plt #引入绘图库
from matplotlib.font_manager import FontProperties 

# Create your views here.
from .models import UserPysicalTest

def body_check(request):
    username = request.session.get("user_name")
    user_name = New_User.objects.get(login_name=username)
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
            BMI = round(heigth / ((hight / 100) ** 2), 2)
            bd = BodyData(user_name=user_name, hight=hight, height=heigth, chest=chest, waist=waist, hip=hip,
                              queith=queith, maxh=maxh,BMI = BMI)
            bd.save()
            DrawdataPic(user_name,"BMI","BMI","BMI指数变化图","BMI")
            DrawdataPic(user_name,"weight","weight","体重变化图","体重(kg)")
            DrawdataPic(user_name,"queith","queith","静息心率变化图","静息心率(bpm)")
            DrawdataPic(user_name,"maxh","maxh","最大心率变化图","最大心率(bpm)")
            messages.success(request,"保存成功")
            return render(request, "wly_app/body.html", locals())
        else:
            error_msg =form.errors
            return render(request,"wly_app/body.html",{'form':form,"errors":error_msg})
    try:    
        bd = BodyData.objects.filter(user_name=user_name).order_by("-createon")[0]
        flag = True
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

#绘制身体数据变化图
def DrawdataPic(user_name,filename,para,title,yname):
    font_set = FontProperties(fname=r"./static/font/MSYH.TTC") 
    datarecord = BodyData.objects.filter(user_name=user_name).order_by("createon")
    data=[]
    time=[]           
    if para=="BMI":
        for record in datarecord:
            data.append(record.BMI)
            time.append(record.createon)
    elif para=="weight":
        for record in datarecord:
            data.append(record.height)
            time.append(record.createon)
    elif para=="queith":
        for record in datarecord:
            data.append(record.queith)
            time.append(record.createon)  
    else:
        for record in datarecord:
            data.append(record.maxh)
            time.append(record.createon)       
    xs = [datetime.strptime(str(d)[0:10],"%Y-%m-%d").date() for d in time]
    plt.figure(dpi=80)
    plt.title(title,fontproperties=font_set,fontsize=17)
    plt.plot(xs,data,'o-')
    plt.xlabel("测试日期",fontproperties=font_set,fontsize=12)
    plt.gcf().autofmt_xdate()
    plt.ylabel(yname,fontproperties=font_set,fontsize=12)
    plt.savefig("./static/img/"+filename+".png")    

def body_pic(request):
    try:
        username = request.session.get("user_name")
        user_name = New_User.objects.get(login_name=username)
        bd = BodyData.objects.filter(user_name=user_name).order_by("-createon")[0]
        BMIfr = "/static/img/BMI.png"
        Wefr = "/static/img/weight.png"
        Queifr = "/static/img/queith.png"
        Maxfr = "/static/img/maxh.png"
    except:
        return redirect("/command/warning2")
    return render(request,"wly_app/bodypic.html",locals())
#体能测试页面
def body_test(request):
    username = request.session.get("user_name")
    user_name = New_User.objects.get(login_name = username)
    bd_finish = False
    abs_finish = False
    pec_finish = False
    cox_finish = False
    limb_finish = False
    ht_finish = False
    try:
        bd_data = BodyData.objects.filter(user_name=user_name)[0]
        bd_finish = True
        hight = bd_data.hight
        height = bd_data.height
        BMI = bd_data.BMI
    except:
        pass
    try:
        partcode = BodyParts.objects.get(partname="腹肌")
        abstest = UserPysicalTest.objects.filter(user_name = user_name,partcode=partcode).count()
        if abstest !=0:
            abs_finish = True
    except:
        pass
    try:
        partcode = BodyParts.objects.get(partname="胸肌")
        pectest = UserPysicalTest.objects.filter(user_name=user_name, partcode=partcode).count()
        if pectest != 0 :
            pec_finish = True
    except:
        pass
    try:
        partcode = BodyParts.objects.get(partname="下肢")
        limbtest = UserPysicalTest.objects.filter(user_name=user_name, partcode=partcode).count()
        if limbtest !=0:
            limb_finish = True
    except:
        pass
    try:
        partcode = BodyParts.objects.get(partname="髋关节")
        coxtest = UserPysicalTest.objects.filter(user_name=user_name, partcode=partcode).count()
        if coxtest !=0:
            cox_finish = True
    except:
        pass
    try:
        partcode = BodyParts.objects.get(partname="心肺")
        hearttest = UserPysicalTest.objects.filter(user_name=user_name, partcode=partcode).count()
        if hearttest !=0:
            ht_finish = True
    except:
        pass
    return render(request,"wly_app/physicaltest.html",locals())

# 腹肌能力测试
def abs_test(request):
    username = request.session.get("user_name")
    if request.method == "POST":
        part_test(request,"腹肌",username,"abs")
        return redirect("/command/test")
    return render(request,"wly_app/abstest.html",locals())

#胸肌能力测试
def pecs_test(request):
    username = request.session.get("user_name")
    if request.method == "POST":
        part_test(request,"胸肌",username,"pec")
        return redirect("/command/test")
    return render(request,"wly_app/pecstest.html",locals())

#下肢能力测试
def limbs_test(request):
    username = request.session.get("user_name")
    if request.method == "POST":
        part_test(request,"下肢",username,"limb")
        return redirect("/command/test")
    return render(request,"wly_app/limbtest.html")

#髋关节能力测试
def cox_test(request):
    username = request.session.get("user_name")
    if request.method == "POST":
        part_test(request,"髋关节",username,"cox")
        return redirect("/command/test")
    return render(request,'wly_app/coxtest.html')

#心肺能力测试
def heart_test(request):
    username = request.session.get("user_name")
    if request.method == "POST":
        part_test(request,"心肺",username,"heart")
        return redirect("/command/test")
    return  render(request,'wly_app/heart.html')

#完成用户的体能测试
def part_test(request,partname,username,paraname):
    user_name = New_User.objects.get(login_name=username)
    testdata = request.POST.get(paraname)
    partcode  = BodyParts.objects.get(partname=partname)
    if partname=="心肺":
        partgrade = GetHeartGrade(partname,testdata)
    else:
        partgrade = GetGrade(partname,testdata)
    partlevel = Getlevel(partgrade)
    # 形成用户的测试数据
    parttest = UserPysicalTest(user_name=user_name, partcode=partcode, testdata=testdata,testlevel=partlevel)
    parttest.save()
    messages.success(request, "测试成功！")


#获取体能力信息
def GetTestInfo(user_name,partname):
    partcode = BodyParts.objects.get(partname=partname)
    partdata = UserPysicalTest.objects.filter(user_name=user_name,partcode=partcode).order_by("-createon")[0].testdata
    cpcomment = TestCompareComment(user_name,partcode)
    if partname=="心肺":
        partgrade = GetHeartGrade(partname,partdata)
        partcomment = GetHeartComment(user_name)
    else:
        partgrade = GetGrade(partname,partdata)
        partcomment = GetComment(user_name,partname)
    partstar = StarShow(partgrade)
    return partgrade,partstar,partcomment,cpcomment

#用户的体测报告
def body_report(request):
    username = request.session.get("user_name")
    # 获取腹肌肌耐力的评分
    user_name = New_User.objects.get(login_name=username)
    try:
        absgrade,absstar,abscomment,abscpcomment = GetTestInfo(username,"腹肌")
        pecgrade,pecstar,peccomment,peccpcomment = GetTestInfo(username,"胸肌")
        limbgrade,limbstar,limbcomment,limbcpcomment = GetTestInfo(username,"下肢")
        coxgrade,coxstar,coxcomment,coxcpcomment = GetTestInfo(username,"髋关节")
        htgrade,heartstar,htcomment,htcpcomment = GetTestInfo(username,"心肺")
        score = ScoreCalculate(absgrade,pecgrade,limbgrade,coxgrade,htgrade)       
        return render(request,'wly_app/bodyreport.html',locals())
    except:
        return redirect("/command/warning")
    return render(request,'wly_app/bodyreport.html',locals())

#获取能力评分
def GetGrade(partname,testdata):
    #拿到用户的能力测试数据
    partcode = BodyParts.objects.get(partname=partname)
    testnum = testdata
    testgrade = BodytestStandard.objects.filter(value__lte=testnum,partcode=partcode).order_by("-points")[0].points
    return testgrade

#获取能力评价
def GetComment(username,partname):
    user_name = New_User.objects.get(login_name=username)
    #拿到用户的能力测试数据
    partcode = BodyParts.objects.get(partname=partname)
    testnum = UserPysicalTest.objects.filter(user_name=user_name,partcode=partcode).order_by("-createon")[0].testdata
    comment = BodytestStandard.objects.filter(value__lte=testnum,partcode=partcode).order_by("-points")[0].comment
    return comment

#获得心肺能力评分
def GetHeartGrade(partname,testdata):
    partcode = BodyParts.objects.get(partname="心肺")
    testnum = testdata
    points = BodytestStandard.objects.filter(value__lte=testnum,partcode=partcode).order_by("points")[0].points
    return points

#获得心肺能力评价
def GetHeartComment(username):
    user_name = New_User.objects.get(login_name=username)
    partcode = BodyParts.objects.get(partname="心肺")
    testnum = UserPysicalTest.objects.filter(user_name=user_name,partcode=partcode).order_by("-createon")[0].testdata
    comment = BodytestStandard.objects.filter(value__lte=testnum,partcode=partcode).order_by("points")[0].comment
    return comment

def Getlevel(grade):
    level = GradeLevel.objects.filter(grade__lte=grade).order_by("-grade")[0].level
    return level

#体测能力星级显示
def StarShow(points):
    stlevel = Getlevel(points)
    stars = starlevel.objects.get(starcode=stlevel)
    star = stars.stardisplay
    return star

#计算总评分
def ScoreCalculate(absgrade,pecgrade,limbgrade,coxgrade,htgrade):
    score = 0.2*absgrade+0.2*pecgrade+0.2*limbgrade+0.2*coxgrade+0.2*htgrade
    return score

#获得最近两次体能测试比较:
def TestCompareComment(user_name,partcode):
    cpcomment = ""
    testnum = UserPysicalTest.objects.filter(user_name=user_name,partcode=partcode).count()
    if testnum >=2:
        prelevel = UserPysicalTest.objects.filter(user_name=user_name,partcode=partcode).order_by("-createon")[1].testlevel
        currlevel = UserPysicalTest.objects.filter(user_name=user_name,partcode=partcode).order_by("-createon")[0].testlevel
        pre = int(prelevel[2])
        curr = int(currlevel[2])
        if curr > pre:
            cpcomment = "比上一次测试提升"+str(curr-pre-1)+"星"
        elif curr == pre:
            cpcomment = "与上一次测试持平"
        else:
            cpcomment = "比上一次测试下降"+str(pre-curr-1)+"星"
    return cpcomment

#体能测试未完成页面
def warning(request):
    return render(request,"wly_app/warning.html")

def warning_two(request):
    return render(request,"wly_app/warning2.html")

#智能训练计划
def trainingplan_recommand(request):
    try:
        username = request.session.get("user_name")
        user_name = New_User.objects.get(login_name=username)
        rccourses = []
        abscourses=GetRcCourse(user_name,"腹肌")
        peccourses=GetRcCourse(user_name,"胸肌")
        coxcourses = GetRcCourse(user_name,"髋关节")
        limbcourses = GetRcCourse(user_name,"下肢")
        htcoureses = GetRcCourse(user_name,"心肺")
        rccourses.extend(abscourses)
        rccourses.extend(peccourses)
        rccourses.extend(coxcourses)
        rccourses.extend(limbcourses)
        rccourses.extend(htcoureses)
        paginator = Paginator(rccourses,2)
        if request.method=="GET":
            page = request.GET.get('page')
            try:
                courses = paginator.page(page)
            except PageNotAnInteger:
                courses = paginator.page(1)
            except InvalidPage:
                courses = paginator.page(1)
            except EmptyPage:
                courses = paginator.page(paginator.num_pages)
    except:
        return redirect("/command/warning")

        
    return render(request,"wly_app/trainingplan.html",locals())

def GetRcCourse(user_name,partname):
    partcode = BodyParts.objects.get(partname=partname)
    coursesid=[]
    coursesname=[]
    desciptions=[]
    frequency=[]
    pic=[]
    partlevel = UserPysicalTest.objects.filter(user_name=user_name,partcode=partcode).order_by("-createon")[0].testlevel
    coursesnum = PartCourse.objects.filter(partcode=partcode,courselevel=partlevel).count()
    courses = PartCourse.objects.filter(partcode=partcode,courselevel=partlevel)
    for i in range(coursesnum):
        coursesid.append(courses[i].courseid.courseid)
        frequency.append(courses[i].frequency)
    for courseid in coursesid:
        coursesname.append(Courses.objects.get(courseid=courseid).coursename)
        desciptions.append(Courses.objects.get(courseid=courseid).decription)
        pic.append(Courses.objects.get(courseid=courseid).pic)
    recourse = list(zip(coursesname,desciptions,frequency,pic))
    
    return recourse
  