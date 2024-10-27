from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from .models import Lesson
from .serializers import LessonSerializer

class LessonViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing lesson instances.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    @extend_schema(
        summary="Create a new lesson",
        description="Add a new lesson to a course by providing the necessary details.",
        request=LessonSerializer,
        responses={201: LessonSerializer},
        tags=["Lessons"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="List all lessons",
        description="Retrieve a list of all lessons available in the system.",
        responses={200: LessonSerializer(many=True)},
        tags=["Lessons"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Retrieve a specific lesson",
        description="Fetch details of a lesson by its ID.",
        responses={200: LessonSerializer},
        parameters=[OpenApiParameter(name="id", description="Lesson ID", required=True, type=int)],
        tags=["Lessons"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Update a lesson",
        description="Modify an existing lesson using its ID.",
        request=LessonSerializer,
        responses={200: LessonSerializer},
        tags=["Lessons"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Partially update a lesson",
        description="Modify specific fields of an existing lesson using its ID.",
        request=LessonSerializer,
        responses={
            200: LessonSerializer,
            404: OpenApiResponse(description="Lesson not found")
        },
        tags=["Lessons"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a lesson",
        description="Remove a lesson by its ID.",
        responses={204: None},
        tags=["Lessons"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
