from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('student','Student'),
        ('instructor','Instructor')
    ]

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='student')
    profile_picture = models.CharField(max_length=255,null=True, blank=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)  

    def __str__(self):
        return f"{self.first_name} ({self.role})"

