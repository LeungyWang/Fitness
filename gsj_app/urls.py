from django.urls import path
from . import views

app_name = 'gsj_app'

urlpatterns = [
    path('course/',views.gsj_test,name='gsj_test'),
    path('coach/',views.gsj_coach,name="gsj_coach"),
    path('info/',views.gsj_info,name="gsj_info")
]