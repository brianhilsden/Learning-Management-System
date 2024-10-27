# models.py
from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course
from users.models import User

User = get_user_model()

class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','course')

    def __str__(self):
        return f"{self.user} enrolled in {self.course}"
