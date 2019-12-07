from django.urls import path
from . import views

app_name = 'ly_app'

urlpatterns = [
    path('course/',views.ly_test,name='ly_test'),
    path('coach/',views.ly_coach,name="ly_coach")
]