from django.db import models

# Create your models here.
class Codes(models.Model):
    code_bytes = models.TextField(null=True,blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.code_bytes


class Students(models.Model):
    student_level = models.CharField(max_length=200,null=True,blank=True)
    student_number = models.CharField(max_length=200,null=True,blank=True)
    student_name = models.CharField(max_length=3,null=True,blank=True,default='000')
    student_nickname = models.CharField(max_length=200,null=True,blank=True)
    student_birthdate = models.CharField(max_length=200,null=True,blank=True)
    student_contact = models.CharField(max_length=200,null=True,blank=True)
    student_leader = models.CharField(max_length=200,null=True,blank=True)
    student_contactleader = models.CharField(max_length=200,null=True,blank=True)
    student_network = models.CharField(max_length=200,null=True,blank=True)

    def __unicode__(self):
        return "[{}] {}".format(self.student_number, self.student_name)

    def __str__(self):
        return "[{}] {}".format(self.student_number, self.student_name)
    
    class Meta:
        get_latest_by = ['student_number']

class AttendanceLifeclass(models.Model):
    class_week = models.CharField(max_length=200,null=True,blank=True)
    student_number = models.CharField(max_length=200,null=True,blank=True)
    student_status = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.student_number

class AttendanceSOL1(models.Model):
    class_week = models.CharField(max_length=200,null=True,blank=True)
    student_number = models.CharField(max_length=200,null=True,blank=True)
    student_status = models.CharField(max_length=200,null=True,blank=True)

class AttendanceSOL2(models.Model):
    class_week = models.CharField(max_length=200,null=True,blank=True)
    student_number = models.CharField(max_length=200,null=True,blank=True)
    student_status = models.CharField(max_length=200,null=True,blank=True)    