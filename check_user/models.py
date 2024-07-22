from django.db import models

# Create your models here.
class UserToken(models.Model):
    phone = models.CharField(max_length=11,null=False,blank=False)
    token = models.CharField(max_length=200,null=False,blank=False)


