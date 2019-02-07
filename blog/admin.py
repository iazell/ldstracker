from django.contrib import admin

from blog.models import Students
from blog.models import AttendanceLifeclass
from blog.models import Network

admin.site.register(Students)
admin.site.register(AttendanceLifeclass)
admin.site.register(Network)
