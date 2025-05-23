from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import date

from rest_framework import viewsets


from .models import (
    Challenge,
    ChallengeProgress,
)

from .serializers import (
    ChallengeSerializer,
    ChallengeProgressSerializer,
)

from users.permissions import IsMentorOrReadOnly


class ChallengeListView(generics.ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ChallengeCreateView(generics.CreateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsMentorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ChallengeDetailView(generics.RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChallengeUpdateView(generics.UpdateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsMentorOrReadOnly]

class ChallengeDeleteView(generics.DestroyAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsMentorOrReadOnly]


# class StartChallengeView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, challenge_id):
#         challenge = Challenge.objects.get(id=challenge_id)
#         progress, created = ChallengeProgress.objects.get_or_create(
#             user=request.user,
#             challenge=challenge
#         )
#         if not created:
#             return Response({"detail": "Вы уже начали этот челлендж."}, status=400)
#         return Response(ChallengeProgressSerializer(progress).data)

# class CompleteDayView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, challenge_id, day):
#         progress = ChallengeProgress.objects.get(user=request.user, challenge_id=challenge_id)
#         if day not in progress.completed_days:
#             progress.completed_days.append(day)
#             progress.current_day = max(progress.current_day, day + 1)
#         if len(progress.completed_days) >= progress.challenge.days:
#             progress.completed_at = timezone.now()
#         progress.save()
#         return Response(ChallengeProgressSerializer(progress).data)
class MyChallengesView(generics.ListAPIView):
    serializer_class = ChallengeProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = ChallengeProgress.objects.filter(user=user)

        completed = self.request.query_params.get('completed')
        if completed is not None:
            if completed.lower() == 'true':
                queryset = queryset.exclude(completed_at__isnull=True)
            elif completed.lower() == 'false':
                queryset = queryset.filter(completed_at__isnull=True)

        return queryset
    
class ChallengeProgressViewSet(viewsets.ModelViewSet):
    queryset = ChallengeProgress.objects.all()
    serializer_class = ChallengeProgressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete_day(self, request, pk=None):
        progress = self.get_object()
        today = date.today().isoformat()

        if progress.user != request.user:
            return Response({"detail": "Access denied."}, status=status.HTTP_403_FORBIDDEN)

        if progress.completed_at:
            return Response({"detail": "Challenge already completed."}, status=status.HTTP_400_BAD_REQUEST)

        if today in progress.completed_days:
            return Response({"detail": "Today already marked as completed."}, status=status.HTTP_400_BAD_REQUEST)

        # Add today's date
        progress.completed_days.append(today)

        # Check for completion
        if len(progress.completed_days) >= progress.challenge.duration_days:
            progress.completed_at = date.today()

        progress.save()
        return Response({"detail": "Day marked as completed."})
    
class ChallengeJoinView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, pk):
        user = request.user
        try:
            challenge = Challenge.objects.get(pk=pk)
        except Challenge.DoesNotExist:
            return Response({"detail": "Challenge not found."}, status=status.HTTP_404_NOT_FOUND)

        progress = challenge.add_user(user)

        if progress is None:
            return Response({"detail": "You are already enrolled in this challenge."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Successfully joined the challenge."}, status=status.HTTP_200_OK)