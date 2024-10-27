from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from .serializers import EnrollmentSerializer
from .models import Enrollment

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing enrollment instances.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary="Create a new enrollment",
        description="Enroll a user in a course by providing the course ID.",
        request=EnrollmentSerializer,
        responses={201: EnrollmentSerializer},
        tags=["Enrollments"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="List all enrollments",
        description="Get a list of all enrollments.",
        responses={200: EnrollmentSerializer(many=True)},
        tags=["Enrollments"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Retrieve a specific enrollment",
        description="Fetch an enrollment by its ID.",
        responses={200: EnrollmentSerializer},
        parameters=[OpenApiParameter(name="id", description="Enrollment ID", required=True, type=int)],
        tags=["Enrollments"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Update an enrollment",
        description="Replace an existing enrollment using its ID.",
        request=EnrollmentSerializer,
        responses={
            200: EnrollmentSerializer,
            404: OpenApiResponse(description="Enrollment not found")
        },
        tags=["Enrollments"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Partially update an enrollment",
        description="Modify specific fields of an existing enrollment using its ID.",
        request=EnrollmentSerializer,
        responses={
            200: EnrollmentSerializer,
            404: OpenApiResponse(description="Enrollment not found")
        },
        tags=["Enrollments"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete an enrollment",
        description="Remove an enrollment by its ID.",
        responses={204: None},
        tags=["Enrollments"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="Get my enrollments",
        description="Retrieve all enrollments for the authenticated user.",
        responses={200: EnrollmentSerializer(many=True)},
        tags=["Enrollments"]
    )
    @action(detail=False, methods=["get"], url_path='my-enrollments')
    def my_enrollments(self, request):
        enrollments = self.queryset.filter(user=request.user)
        serializer = self.get_serializer(enrollments, many=True)
        return Response(serializer.data)
