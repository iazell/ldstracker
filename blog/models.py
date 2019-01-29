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
    
    class Meta:
        get_latest_by = ['student_number']