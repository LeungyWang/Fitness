from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('regist/',views.user_regist,name='user_regist'),
    path('index/',views.user_login,name='user_login'),
]