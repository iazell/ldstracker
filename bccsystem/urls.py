from django.urls import path
from . import views
from django.contrib import admin
from .views import (
    StudentList,
    AttendanceStudentLifeclass,
    AttendanceStudentSOL1,
    AttendanceStudentSOL2)

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate, name='generate'),
    path('addstudent/', views.addstudent),
    path('lifeclassstudents/', views.lifeclassstudents),
    path('sol1students/', views.sol1students),
    path('sol2students/', views.sol2students),
    path('searchStudent/', views.searchStudent),
    path('editstudent/', views.editstudent),

    path('admin/', admin.site.urls),
    path('getstudents/', StudentList.as_view(), name='api-students'),
    path('postattendancelifeclass/', AttendanceStudentLifeclass.as_view(), name='api-attendancelifeclass-students'),
    path('postattendancesol1/', AttendanceStudentSOL1.as_view(), name='api-attendancesol1-students'),
    path('postattendancesol2/', AttendanceStudentSOL2.as_view(), name='api-attendancesol2-students'),
]
