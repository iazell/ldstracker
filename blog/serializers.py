from rest_framework import serializers
from .models import (
    Students,
    AttendanceLifeclass
)

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class AttendanceStudentSerializer(serializers.ModelSerializer):
	class Meta:
	  model = AttendanceLifeclass
	  fields = '__all__'