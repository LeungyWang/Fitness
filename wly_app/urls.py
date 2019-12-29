from django.urls import path
from . import views

app_name = 'wly_app'

urlpatterns=[
    path('body/', views.body_check, name='body_check'),
    path('test/',views.body_test,name='body_test'),
    path('test/abs/',views.abs_test,name='abs_test'),
    path('test/pecs/',views.pecs_test,name='pecs_test'),
    path("test/limb/",views.limbs_test,name='limb_test'),
    path('test/cox/',views.cox_test,name='cox_test'),
    path('test/heart',views.heart_test,name='heart_test'),
    path('bodyreport',views.body_report,name='body_report'),
    path('warning',views.warning,name='warning'),
    path('trainingplan',views.trainingplan_recommand,name='trainingplan'),
    path('body/bodypic',views.body_pic,name="bodypic"),
    path('warning2',views.warning_two,name='warning2'),
    path('pytestmanage',views.pytest_manage,name='pytestmanage'),
    path('test/addtest',views.addtest,name='addtest'),
    path('<str:partcode>/delete',views.deletetest,name='deletetest'),
    path('<str:partcode>/edit',views.edittest,name='edittest'),
    path('coursemanage',views.coursemanage,name='coursemanage'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('course/<str:courseid>/delete',views.deletecourse,name='deletetest'),
    path('course/<str:courseid>/edit',views.editcourse,name='editcourse'),
]

