from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Forum(models.Model):
    """
    Represents a specific discussion forum or topic.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums')

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Represents a message or comment within a forum.
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post by {self.user.username} in {self.forum.title}"


class Comment(models.Model):
    """
    Represents replies to a post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"
