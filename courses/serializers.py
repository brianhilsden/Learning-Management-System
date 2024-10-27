from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Course

User = get_user_model()

class CoursesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email', 'role') 


class CourseSerializer(serializers.ModelSerializer):
    instructor = CoursesUserSerializer(allow_null=True, read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='instructor'), source='instructor',allow_null=False,required=True)
    class Meta:
        model = Course
        fields = ("id","title","description","duration","level","instructor","instructor_id","created_at","updated_at")



