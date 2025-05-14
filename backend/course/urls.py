from django.urls import path
from .views import *

<<<<<<< HEAD
=======
challenge_progress_list = ChallengeProgressViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

challenge_progress_detail = ChallengeProgressViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

>>>>>>> a461d6aa94722e7934a74d9f31b09a7f1e1c23a6
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

<<<<<<< HEAD
    path('courses/<int:course_id>/complete/', CompleteCourseView.as_view(), name='complete-course'),
    path('courses/<int:course_id>/certificate/', CourseCertificateView.as_view(), name='course-certificate'),
    path("certificates/<str:username>/<int:course_id>/", certificate_share_view, name="certificate-share"),

=======
    # challenge
    path('challenges/', ChallengeListView.as_view(), name='challenge-list'),
    path('challenge/create/', ChallengeCreateView.as_view(), name='challenge-create'),
    path('challenge/<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),
    path('challenge/<int:pk>/update/', ChallengeUpdateView.as_view(), name='challenge-update'),
    path('challenge/<int:pk>/delete/', ChallengeDeleteView.as_view(), name='challenge-delete'),
    path('challenge/<int:challenge_id>/start/', StartChallengeView.as_view(), name='challenge-start'),
    path('challenge/my/', MyChallengesView.as_view(), name='my-challenges'),
    path('challenge/<int:pk>/join/', ChallengeJoinView.as_view(), name='challenge-join'),
    path('challenge-progress/', challenge_progress_list, name='challenge-progress-list'),
    path('challenge-progress/<int:pk>/', challenge_progress_detail, name='challenge-progress-detail'),
>>>>>>> a461d6aa94722e7934a74d9f31b09a7f1e1c23a6
]
