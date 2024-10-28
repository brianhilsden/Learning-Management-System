from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()
# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="quizes")
    instructions = models.TextField(blank=True, null=True)
    duration_minutes = models.IntegerField()
    instructor = models.ForeignKey(User,on_delete=models.SET_NULL,limit_choices_to={'role':'instructor'},null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[('MCQ', 'Multiple Choice'), ('TXT', 'Text')])

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class StudentQuizAttempt(models.Model):
    student = models.ForeignKey(User, related_name='quiz_attempts', on_delete=models.CASCADE, limit_choices_to={'role':'student'})
    quiz = models.ForeignKey(Quiz, related_name='attempts', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)