from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrollmentsViewSet

router = DefaultRouter()
router.register(r'', EnrollmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
