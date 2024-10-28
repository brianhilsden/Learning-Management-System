from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ForumViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'forums', ForumViewSet, basename='forum')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('forums/<int:pk>/posts/', ForumViewSet.as_view({'get': 'get_posts'}), name='forum-posts'),
    path('posts/<int:pk>/comments/', PostViewSet.as_view({'get': 'get_comments'}), name='post-comments'),
]
