from django.urls import path
from .views import *

urlpatterns = [
    # Курсы
    path('course/', CourseListView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/create/', CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

    # Прогресс
    path('progress/', CourseProgressListCreateView.as_view(), name='course-progress'),
    path('progress/<int:pk>/update/', CourseProgressUpdateView.as_view(), name='course-progress-update'),

    # Уроки
    path('<int:course_id>/lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    # Квизы
    path('lessons/<int:lesson_id>/quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),

    # challenge
    path('', ChallengeListView.as_view(), name='challenge-list'),
    path('challenge/create/', ChallengeCreateView.as_view(), name='challenge-create'),
    path('challenge/<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),
    path('challenge/<int:pk>/update/', ChallengeUpdateView.as_view(), name='challenge-update'),
    path('challenge/<int:pk>/delete/', ChallengeDeleteView.as_view(), name='challenge-delete'),
    path('challenge/<int:challenge_id>/start/', StartChallengeView.as_view(), name='challenge-start'),
    path('challenge/<int:challenge_id>/complete/<int:day>/', CompleteDayView.as_view(), name='challenge-complete-day'),

]
