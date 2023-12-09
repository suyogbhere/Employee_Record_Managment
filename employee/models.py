from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee_Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=100, null=True)
    empdept = models.CharField(max_length=100, null= True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null= True)
    joining_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username 
    


class Employee_Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100, null=True)
    schoolclgpg = models.CharField(max_length=100, null= True)
    yearofpassingpg = models.CharField(max_length=20, null=True)
    percentagepg = models.CharField(max_length=30, null=True)
    coursegra = models.CharField(max_length=100, null=True)
    schoolclgra = models.CharField(max_length=100, null= True)
    yearofpassinggra = models.CharField(max_length=20, null=True)
    percentagegra = models.CharField(max_length=30, null=True)
    coursessc = models.CharField(max_length=100, null=True)
    schoolclgssc = models.CharField(max_length=100, null= True)
    yearofpassingssc = models.CharField(max_length=20, null=True)
    percentagessc = models.CharField(max_length=30, null=True)
    coursegrahsc = models.CharField(max_length=100, null=True)
    schoolclhsc = models.CharField(max_length=100, null= True)
    yearofpassinghsc = models.CharField(max_length=20, null=True)
    percentagehsc = models.CharField(max_length=30, null=True)

    joining_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username 
    

class Employee_Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100, null=True)
    company1desig = models.CharField(max_length=100, null= True)
    company1salary = models.CharField(max_length=100, null=True)
    company1duration = models.CharField(max_length=100, null=True)
    company2name = models.CharField(max_length=100, null=True)
    company2desig = models.CharField(max_length=100, null= True)
    company2salary = models.CharField(max_length=100, null=True)
    company2duration = models.CharField(max_length=100, null=True)
    company3name = models.CharField(max_length=100, null=True)
    company3desig = models.CharField(max_length=100, null= True)
    company3salary = models.CharField(max_length=100, null=True)
    company3duration = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username 