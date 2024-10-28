from rest_framework import serializers
from .models import Forum, Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Post
        fields = '__all__'

class ForumSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Forum
        fields = '__all__'
