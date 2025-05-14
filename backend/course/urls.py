from django.urls import path
from .views import *

urlpatterns = [
    # Курсы
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/create/', CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

    # Прогресс
    path('course/progress/', CourseProgressListCreateView.as_view(), name='course-progress'),
    path('progress/<int:pk>/update/', CourseProgressUpdateView.as_view(), name='course-progress-update'),

    # Уроки
    path('courses/<int:course_id>/lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    # Квизы
    path('lessons/<int:lesson_id>/quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),

    path('courses/<int:course_id>/complete/', CompleteCourseView.as_view(), name='complete-course'),
    path('courses/<int:course_id>/certificate/', CourseCertificateView.as_view(), name='course-certificate'),
    path("certificates/<str:username>/<int:course_id>/", certificate_share_view, name="certificate-share"),

]
