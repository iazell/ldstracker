from rest_framework import serializers
from .models import (
    Students,
    AttendanceLifeclass,
    AttendanceSOL1,
    AttendanceSOL2
)

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class AttendanceStudentLifeclassSerializer(serializers.ModelSerializer):
	class Meta:
	  model = AttendanceLifeclass
	  fields = '__all__'

class AttendanceStudentSOL1Serializer(serializers.ModelSerializer):
	class Meta:
	  model = AttendanceSOL1
	  fields = '__all__'


class AttendanceStudentSOL2Serializer(serializers.ModelSerializer):
	class Meta:
	  model = AttendanceSOL2
	  fields = '__all__'