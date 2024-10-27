from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Lesson

User = get_user_model()

class LessonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email', 'role') 



class LessonSerializer(serializers.ModelSerializer):
    instructor = LessonUserSerializer(allow_null=True, read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='instructor'), source='instructor',allow_null=True,required=False)
    class Meta:
        model = Lesson
        fields = ('id', 'course', 'title', 'description', 'content','instructor','instructor_id', 'created_at', 'updated_at')
