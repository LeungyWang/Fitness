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
]

