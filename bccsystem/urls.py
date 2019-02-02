from django.urls import path
from . import views
from django.contrib import admin

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
]