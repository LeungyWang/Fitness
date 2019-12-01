from django.urls import path
from . import views

app_name = 'wly_app'

urlpatterns=[
    path('body/', views.body_check, name='user_login'),

]

