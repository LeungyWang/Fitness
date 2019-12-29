from django.urls import path
from . import views

app_name = 'ly_app'

urlpatterns = [
    path('course/',views.ly_test,name='ly_test'),
    path('course_in/',views.ly_course_in,name='ly_course_in'),
    path('coach/',views.ly_coach,name="ly_coach"),
    path('coach_in/', views.ly_coach_in, name="ly_coach_in"),
    path('info/',views.ly_info,name="ly_info"),
    path('course_choose/', views.course_choose, name="course_choose"),
    path('coach_choose/', views.coach_choose, name="coach_choose"),
    path('info_save/', views.save_info, name="info_save"),
    path('course_del/', views.course_del, name="course_del"),
    path('course_edit/', views.course_edit, name="course_edit"),
    path('UserCourse_del/',views.UserCourse_del,name="UserCourse_del"),
    path('UserCoach_del/',views.UserCoach_del,name="UserCoach_del"),
    path('coach_del/',views.coach_del,name="coach_del"),
    path('coach_edit/',views.coach_edit,name="coach_edit")

]