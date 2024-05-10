from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20) 
    description = models.TextField(max_length=20) 
    status = models.IntegerField(max_length=20) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField(max_length=20,null=True) 
    description = models.TextField(max_length=20,null=True) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    firstname = models.TextField(max_length=20) 
    middlename = models.TextField(max_length=20,blank=True,null= True) 
    lastname = models.TextField(max_length=20) 
    gender = models.TextField(max_length=20,blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField(max_length=20) 
    address = models.TextField(max_length=20) 
    email = models.TextField(max_length=20) 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '