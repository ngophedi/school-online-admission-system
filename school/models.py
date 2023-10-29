from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name


courses = [
    ('IT', 'IT'),
    ('Plumbing', 'Plumbing'),
    ('Electrical', 'Electrical'),
 
]

classes=[('Module1','Module1')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='Module1')
    course = models.CharField(max_length=10, choices=courses, default='IT')
    national_id = models.CharField(max_length=20, null=True)  # Add the national ID field
    parent_name = models.CharField(max_length=100, null=True)  # Add the parent name field
    parent_mobile = models.CharField(max_length=40, null=True)  # Add the parent mobile number field
    profile_image = models.FileField(upload_to='static/images/', null=True, blank=True)



    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name 
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)
