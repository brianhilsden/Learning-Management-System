from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse

from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer   
    permission_classes = [AllowAny]

    @extend_schema(
        summary="List all users",
        description="Retrieve a list of all registered users in the system.",
        responses={200: UserSerializer(many=True)},
        tags=["Users"]
    )
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to list all users.
        """
        return super().get(request, *args, **kwargs)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    @extend_schema(
        summary="Register a new user",
        description="Register a new user and obtain JWT tokens for authentication.",
        request=RegisterSerializer,
        responses={
            201: OpenApiResponse(response=UserSerializer, description="User registered successfully and tokens generated."),
            400: OpenApiResponse(description="Validation errors occurred during registration.")
        },
        tags=["Users"]
    )
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to register a new user.
        Generates JWT tokens upon successful registration.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save the user instance
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        
        # Prepare the response data
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'role': user.role,
                'profile_picture': user.profile_picture,
            }
        }, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @extend_schema(
        summary="Obtain JWT tokens",
        description="Login with email and password to obtain JWT tokens for authentication.",
        responses={
            200: OpenApiResponse(description="Tokens generated successfully."),
            400: OpenApiResponse(description="Invalid credentials provided.")
        },
        tags=["Users"]
    )
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for user login.
        Validates credentials and returns JWT tokens.
        """
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
            'profile_picture': user.profile_picture
        })
    

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Retrieve user profile",
        description="Retrieve profile details of the authenticated user.",
        responses={200: UserSerializer},
        tags=["Users"]
    )
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to retrieve the profile of the authenticated user.
        """
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
