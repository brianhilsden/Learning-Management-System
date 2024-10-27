from rest_framework import serializers
from .models import Enrollment

from courses.models import Course

class EnrollmentsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'duration', 'level', 'instructor', 'created_at', 'updated_at')



class EnrollmentSerializer(serializers.ModelSerializer):
    course = EnrollmentsCourseSerializer(read_only=True) 
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course')  # Accept course ID
    class Meta:
        model = Enrollment
        fields = ('id', 'user', 'course','course_id', 'created_at')