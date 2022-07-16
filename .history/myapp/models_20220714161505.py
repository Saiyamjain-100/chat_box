from statistics import mode
from django.db import models
from datetime import datetime

# Create your models here.
class room(models.Model):
    name = models.CharField(max_length=10000)

class message(models.Model):
    value = models.CharField(max_length=1000000)
    date= models.DateTimeField(default=datetime.now,blank=True)
    room =models.CharField(max_length=10000)
    user =models.CharField(max_length=10000)
    img 