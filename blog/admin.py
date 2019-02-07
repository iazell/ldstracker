from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from blog.models import Students
from blog.models import AttendanceLifeclass
from blog.models import AttendanceSOL1
from blog.models import AttendanceSOL2
from blog.models import Network

from bccsystem.resources import StudentResource

# admin.site.register(Students)
admin.site.register(AttendanceLifeclass)
admin.site.register(AttendanceSOL1)
admin.site.register(AttendanceSOL2)
admin.site.register(Network)

@admin.register(Students)
class StudentAdmin(ImportExportModelAdmin):
    pass