from django.contrib import admin
from .models import Forum,Comment,Post
# Register your models here.
admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Post)