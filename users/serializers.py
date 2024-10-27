from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name','last_name', 'email', 'role', 'profile_picture')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    username = serializers.CharField(allow_blank=True, required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    profile_picture = serializers.CharField(required=False, allow_blank=True)
    role = serializers.ChoiceField(choices=[('admin', 'Admin'), ('student', 'Student'), ('instructor', 'Instructor')], default='student')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'role', 'profile_picture')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            role=validated_data['role'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data.get('username') 
        )
        if validated_data.get('profile_picture'):
            user.profile_picture = validated_data["profile_picture"]
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('No user found with this email address.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid password.')

        attrs['user'] = user
        return attrs
        
