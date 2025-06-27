from rest_framework import viewsets
from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def student_quiz_score(request, student_id, quiz_id):
    answers = StudentAnswer.objects.filter(
        student_id=student_id,
        question__quiz_id=quiz_id
    )

    total_questions = answers.count()
    correct_answers = 0

    for ans in answers:
        if ans.selected_answer.is_correct:
            correct_answers += 1

    return Response({
        "student_id": student_id,
        "quiz_id": quiz_id,
        "total_questions_answered": total_questions,
        "correct_answers": correct_answers,
        "score_percentage": f"{(correct_answers / total_questions * 100) if total_questions else 0:.2f}%"
    })
