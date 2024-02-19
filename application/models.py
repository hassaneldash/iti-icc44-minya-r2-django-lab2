from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=200, default='')
    lname = models.CharField(max_length=200, default='')
    uname = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=200)
    s_email = models.EmailField(max_length=200)
    age = models.IntegerField()
