from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, StudentQuizAttemptViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'quiz-attempts', StudentQuizAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
