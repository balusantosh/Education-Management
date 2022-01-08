from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField( null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=16, null=True, blank=True)
    rollno = models.IntegerField()
    college_name = models.CharField(max_length=100)
    phone_no = models.CharField(unique=True , max_length=10)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['complete']

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField( null=True, blank=True)  

    def __str__(self):
        return self.title

class Notification(models.Model):
    title =models.CharField(max_length=20)
    description =models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
    