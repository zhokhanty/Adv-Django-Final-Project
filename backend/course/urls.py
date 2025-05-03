from django.urls import path
from .views import *

urlpatterns = [
    # Курсы
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

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
    path('create/', ChallengeCreateView.as_view(), name='challenge-create'),
    path('<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),
    path('<int:pk>/update/', ChallengeUpdateView.as_view(), name='challenge-update'),
    path('<int:pk>/delete/', ChallengeDeleteView.as_view(), name='challenge-delete'),
    path('<int:challenge_id>/start/', StartChallengeView.as_view(), name='challenge-start'),
    path('<int:challenge_id>/complete/<int:day>/', CompleteDayView.as_view(), name='challenge-complete-day'),

]
