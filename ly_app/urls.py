from django.urls import path
from . import views

app_name = 'ly_app'

urlpatterns = [
    path('test/',views.ly_test,name='ly_test'),
]