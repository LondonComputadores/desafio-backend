from django.urls import path
from .views import Quiz, RandomQuestion, QuizQuestion, StartQuiz


app_name='quizapp'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('question/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
    path('single/<str:title>/', StartQuiz.as_view(), name='quiz'),
]