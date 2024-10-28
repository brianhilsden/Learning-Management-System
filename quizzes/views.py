from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Quiz, StudentQuizAttempt, Answer
from .serializers import QuizSerializer, QuizListSerializer, StudentQuizAttemptDetailSerializer, SubmitQuizSerializer,CreateQuizAttemptSerializer
from django.utils import timezone
from drf_spectacular.utils import extend_schema

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return QuizListSerializer
        return QuizSerializer

    @extend_schema(
        summary='List all quizzes',
        responses={200: QuizListSerializer(many=True)},
        tags=["Quizzes"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary='Retrieve a quiz',
        responses={200: QuizSerializer},
        tags=["Quizzes"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary='Create a new quiz',
        request=QuizSerializer,
        responses={201: QuizSerializer},
        tags=["Quizzes"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary='Update a quiz',
        request=QuizSerializer,
        responses={200: QuizSerializer},
        tags=["Quizzes"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary='Partially update a quiz',
        request=QuizSerializer,
        responses={200: QuizSerializer},
        tags=["Quizzes"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary='Delete a quiz',
        responses={204: None},
        tags=["Quizzes"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class StudentQuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = StudentQuizAttempt.objects.all()
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='List quiz attempts for the authenticated student',
        responses={200: StudentQuizAttemptDetailSerializer(many=True)},
        tags=["Quiz attempt"]
    )
    def list(self, request, *args, **kwargs):
        attempts = StudentQuizAttempt.objects.filter(student=request.user)
        serializer = StudentQuizAttemptDetailSerializer(attempts, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary='Retrieve a specific quiz attempt',
        responses={200: StudentQuizAttemptDetailSerializer},
        tags=["Quiz attempt"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary='Create a new quiz attempt for the authenticated student',
        request=CreateQuizAttemptSerializer,
        responses={201: StudentQuizAttemptDetailSerializer},
        tags=["Quiz attempt"]
    )
    def create(self, request, *args, **kwargs):
        # Use the quiz ID from the validated data
        serializer = CreateQuizAttemptSerializer(data=request.data)
        if serializer.is_valid():
            quiz = serializer.validated_data['quiz']
            attempt, created = StudentQuizAttempt.objects.get_or_create(student=request.user, quiz=quiz)
            if not created:
                return Response({"detail": "Quiz already attempted."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(StudentQuizAttemptDetailSerializer(attempt).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary='Update a quiz attempt',
        request=StudentQuizAttemptDetailSerializer,
        responses={200: StudentQuizAttemptDetailSerializer},
        tags=["Quiz attempt"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary='Partially update a quiz attempt',
        request=StudentQuizAttemptDetailSerializer,
        responses={200: StudentQuizAttemptDetailSerializer},
        tags=["Quiz attempt"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary='Delete a quiz attempt',
        responses={204: None},
        tags=["Quiz attempt"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary='Submit a list of answer IDs for a quiz attempt and get back data including scores',
        request=SubmitQuizSerializer,
        responses={200: StudentQuizAttemptDetailSerializer},
        tags=["Quiz attempt"]
    )
    @action(detail=True, methods=['post'], url_path='submit')
    def submit_attempt(self, request, pk=None):
        quiz = Quiz.objects.get(pk=pk)
        attempt = StudentQuizAttempt.objects.get(student=request.user, quiz=quiz)

        if attempt.completed:
            return Response({"detail": "Quiz already completed."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SubmitQuizSerializer(data=request.data)
        if serializer.is_valid():
            submitted_answers = serializer.validated_data['submitted_answers']
            score = calculate_score(quiz, submitted_answers)

            attempt.score = score
            attempt.completed = True
            attempt.completed_at = timezone.now()
            attempt.save()

            return Response(StudentQuizAttemptDetailSerializer(attempt).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def calculate_score(quiz, submitted_answers):
    correct_answers = Answer.objects.filter(question__quiz=quiz, is_correct=True)

    if not correct_answers.exists():
        return 0

    score = 0

    # Iterate through the correct answers and check if submitted answers match
    for answer in correct_answers:
        if answer.id in submitted_answers:
            score += 1

    # Calculate the percentage score
    return (score / len(correct_answers)) * 100
