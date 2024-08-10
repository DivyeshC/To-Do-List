from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime,date
# Create your models here.

class TODO(models.Model):
    status_choices = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ]
    priority_choices = [
    
    ('1-High','High'),
    ('2-Medium','Medium'),
    ('3-Low','Low'),
    
    ]
    title=models.CharField(max_length=350)
    status = models.CharField(max_length=100 , choices=status_choices)
    priority= models.CharField(max_length=100 , choices=priority_choices)
    user= models.ForeignKey(User , on_delete=models.CASCADE)
    last_date=models.DateField(default=datetime.now)
    
