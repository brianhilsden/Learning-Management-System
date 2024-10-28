# serializers.py
from rest_framework import serializers
from .models import Quiz, Question, Answer, StudentQuizAttempt

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'answers']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'instructions', 'duration_minutes', 'questions','course_id']

    def create(self, validated_data):
        # Extract questions data
        questions_data = validated_data.pop('questions')
        course_id = validated_data.pop('course_id')
        
        # Create the quiz object
        quiz = Quiz.objects.create(course_id=course_id,**validated_data)
        
        # Create questions and answers
        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = Question.objects.create(quiz=quiz, **question_data)
            
            # Create answers associated with each question
            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        return quiz

class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'instructions', 'duration_minutes']

class CreateQuizAttemptSerializer(serializers.Serializer):
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all(), required=True)

class SubmitQuizSerializer(serializers.Serializer):
    submitted_answers = serializers.ListField(
        child=serializers.IntegerField()
    )


class StudentQuizAttemptDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentQuizAttempt
        fields = ['id', 'quiz', 'student', 'score', 'completed', 'started_at', 'completed_at']
        read_only_fields = ['quiz', 'student', 'score', 'completed', 'completed_at']  

