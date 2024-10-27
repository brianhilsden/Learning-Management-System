from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced')
    ]
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    duration = models.DurationField()
    level = models.CharField(max_length=20,choices=LEVEL_CHOICES)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title