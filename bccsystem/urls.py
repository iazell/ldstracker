from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('index/', views.home, name='home'),
    path('generate/', views.generate, name='generate'),
    path('print/', views.print, name='print'),
    path('addstudent/', views.addstudent),
    path('studentstab/', views.studentstab),
    path('admin/', admin.site.urls),
]