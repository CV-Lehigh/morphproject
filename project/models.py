from django.db import connections
from django.db import models
from PIL import Image
from django.conf import settings


'''
class Image(models.Model):
    
    image=models.ImageField(upload_to="settings.MEDIA_ROOT/chicago")
    file_type = models.CharField(max_length=256, choices=[('image', 'image'), ('video', 'video'), ('other', 'other')])
    #title = "hello"
    #def __str__(self):
    #    return self.title
    class Meta:
        db_table="image_upload"
        '''

class EmployeeDetails(models.Model):
    empname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    # class Meta:
        # db_table="empdetails"


# models.py
# all uploaded images will be stored in media/up-load
# for testing images
class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')

########## new models for the final version

class Image(models.Model):
    folder = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)
    imageFile = models.ImageField(upload_to='upload/')
    index = models.IntegerField()

class Folder(models.Model):
    folder = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)

class Task(models.Model):
    folder = models.CharField(max_length=50)
    indexStop = models.IntegerField()
    user = models.CharField(max_length=50)
    order = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    sexAssign = models.CharField(max_length=50)
    order = models.CharField(max_length=50)
    tasksDone = models.IntegerField()