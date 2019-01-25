from django.db import models

# Create your models here.
class Students(models.Model):
    firstName = models.CharField(max_length=200,null=True,blank=True)
    lastName = models.CharField(max_length=200,null=True,blank=True)
    agentCode = models.CharField(max_length=200,null=True,blank=True)
    mobileNumber = models.CharField(max_length=200,null=True,blank=True)
    deviceKey = models.CharField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=200,null=True,blank=True)
    dateCreated = models.CharField(max_length=200,null=True,blank=True)
    
    class Meta:
        app_label = 'tracker'