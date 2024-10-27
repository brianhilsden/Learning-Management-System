from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from .serializers import CourseSerializer
from lessons.serializers import LessonSerializer
from .models import Course

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @extend_schema(
        summary="Retrieve a specific course",
        description="Fetch a course by its ID.",
        responses={200: CourseSerializer},
        parameters=[OpenApiParameter(name="id", description="Course ID", required=True, type=int)],
        tags=["Courses"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="List all courses",
        description="Get a list of all available courses.",
        responses={200: CourseSerializer(many=True)},
        tags=["Courses"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new course",
        description="Add a new course with necessary details.",
        request=CourseSerializer,
        responses={201: CourseSerializer},
        tags=["Courses"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Update a course",
        description="Replace an existing course using its ID.",
        request=CourseSerializer,
        responses={
            200: CourseSerializer,
            404: OpenApiResponse(description="Course not found")
        },
        tags=["Courses"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Partially update a course",
        description="Modify specific fields of an existing course using its ID.",
        request=CourseSerializer,
        responses={
            200: CourseSerializer,
            404: OpenApiResponse(description="Course not found")
        },
        tags=["Courses"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a course",
        description="Remove a course by its ID.",
        responses={204: None},
        tags=["Courses"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="Get lessons associated with a course",
        description="Retrieve all lessons related to a specific course by its ID.",
        responses={200: LessonSerializer(many=True)},
        parameters=[OpenApiParameter(name="pk", description="Course ID", required=True, type=int)],
        tags=["Courses"]
    )
    @action(detail=True, methods=['get'], url_path='lessons')
    def get_lessons(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        lessons = course.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
