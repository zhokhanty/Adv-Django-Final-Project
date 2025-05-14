from django.urls import path
from .views import *

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

urlpatterns = [
    # challenge
    path('challenges/', ChallengeListView.as_view(), name='challenge-list'),
    path('challenge/create/', ChallengeCreateView.as_view(), name='challenge-create'),
    path('challenge/<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),
    path('challenge/<int:pk>/update/', ChallengeUpdateView.as_view(), name='challenge-update'),
    path('challenge/<int:pk>/delete/', ChallengeDeleteView.as_view(), name='challenge-delete'),
    path('challenge/my/', MyChallengesView.as_view(), name='my-challenges'),
    path('challenge/<int:pk>/join/', ChallengeJoinView.as_view(), name='challenge-join'),
    path('challenge-progress/', challenge_progress_list, name='challenge-progress-list'),
    path('challenge-progress/<int:pk>/', challenge_progress_detail, name='challenge-progress-detail'),

]