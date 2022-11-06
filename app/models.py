from django.db import models


class EnquiryModel(models.Model):
    eno = models.AutoField(primary_key=True,default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.IntegerField(unique=True)
    message = models.CharField(max_length=300)


class CareerModel(models.Model):
    cno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(unique=True)
    qualification = models.CharField(max_length=100)
    dob = models.DateField()
    experience = models.IntegerField()
    designation = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/',default=False)




