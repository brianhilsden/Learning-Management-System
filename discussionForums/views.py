from rest_framework import viewsets
from rest_framework.response import Response
from .models import Forum, Post, Comment
from .serializers import ForumSerializer, PostSerializer, CommentSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(
        description="Retrieve a list of forums.",
        summary="List all discussion forums.",
        tags=["Forum"]
    ),
    create=extend_schema(
        description="Create a new forum.",
        summary="Create a new forum.",
        tags=["Forum"]
    ),
    retrieve=extend_schema(
        description="Retrieve a specific forum by ID.",
        summary="Get forum details.",
        tags=["Forum"]
    ),
    update=extend_schema(
        description="Update a specific forum by ID.",
        summary="Update forum details.",
        tags=["Forum"]
    ),
    partial_update=extend_schema(
        description="Partially update a specific forum by ID.",
        summary="Partially update forum information.",
        tags=["Forum"]
    ),
    destroy=extend_schema(
        description="Delete a specific forum by ID.",
        summary="Delete a forum.",
        tags=["Forum"]
    ),
)
class ForumViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing forums.
    """
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

    @extend_schema(
        responses={200: PostSerializer(many=True)},
        description="Get all posts under a specific forum.",
        summary="List all posts in a forum."
    )
    def get_posts(self, request, pk=None):
        """
        Get all posts under a specific forum.
        """
        forum = self.get_object()
        posts = forum.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@extend_schema_view(
    list=extend_schema(
        description="Retrieve a list of posts.",
        summary="List all posts.",
        tags=["Post - forum"]
    ),
    create=extend_schema(
        description="Create a new post.",
        summary="Create a new post.",
        tags=["Post - forum"]
    ),
    retrieve=extend_schema(
        description="Retrieve a specific post by ID.",
        summary="Get post details.",
        tags=["Post - forum"]
    ),
    update=extend_schema(
        description="Update a specific post by ID.",
        summary="Update post details.",
        tags=["Post - forum"]
    ),
    partial_update=extend_schema(
        description="Partially update a specific post by ID.",
        summary="Partially update post information.",
        tags=["Post - forum"]
    ),
    destroy=extend_schema(
        description="Delete a specific post by ID.",
        summary="Delete a post.",
        tags=["Post - forum"]
    ),
)
class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    @extend_schema(
        responses={200: CommentSerializer(many=True)},
        description="Get all comments under a specific post.",
        summary="List all comments on a post."
    )
    def get_comments(self, request, pk=None):
        """
        Get all comments under a specific post.
        """
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@extend_schema_view(
    list=extend_schema(
        description="Retrieve a list of comments.",
        summary="List all comments.",
        tags=["Comments - forum"]
    ),
    create=extend_schema(
        description="Create a new comment.",
        summary="Create a new comment.",
        tags=["Comments - forum"]
    ),
    retrieve=extend_schema(
        description="Retrieve a specific comment by ID.",
        summary="Get comment details.",
        tags=["Comments - forum"]
    ),
    update=extend_schema(
        description="Update a specific comment by ID.",
        summary="Update comment details.",
        tags=["Comments - forum"]
    ),
    partial_update=extend_schema(
        description="Partially update a specific comment by ID.",
        summary="Partially update comment information.",
        tags=["Comments - forum"]
    ),
    destroy=extend_schema(
        description="Delete a specific comment by ID.",
        summary="Delete a comment.",
        tags=["Comments - forum"]
    ),
)
class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


