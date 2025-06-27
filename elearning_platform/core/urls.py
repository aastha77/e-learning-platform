from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import student_quiz_score
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'student-answers', StudentAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:student_id>/quiz/<int:quiz_id>/score/', student_quiz_score, name='student-quiz-score'),
]
