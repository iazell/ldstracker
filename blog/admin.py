from django.contrib import admin

from blog.models import Students
from blog.models import AttendanceLifeclass
from blog.models import AttendanceSOL1
from blog.models import AttendanceSOL2
from blog.models import Network

admin.site.register(Students)
admin.site.register(AttendanceLifeclass)
admin.site.register(AttendanceSOL1)
admin.site.register(AttendanceSOL2)
admin.site.register(Network)
