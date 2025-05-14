from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from rest_framework.decorators import api_view, permission_classes
from django.utils.timezone import now
from rest_framework import viewsets


from .models import (
    Course,
    Lesson,
    Quiz,
    CourseProgress,
    Challenge,
    ChallengeProgress,
)

from .serializers import (
    CourseSerializer,
    LessonSerializer,
    QuizSerializer,
    CourseProgressSerializer,
    ChallengeSerializer,
    ChallengeProgressSerializer,
)

from users.permissions import IsMentorOrReadOnly

# ==== КУРСЫ ====
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsMentorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsMentorOrReadOnly]

class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsMentorOrReadOnly]


# ==== LESSON ====

class LessonListCreateView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Lesson.objects.filter(course_id=course_id)

    def get(self, request, *args, **kwargs):
        lessons = self.get_queryset()
        serializer = self.get_serializer(lessons, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id')
        serializer.save(course_id=course_id)

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsMentorOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Lesson.objects.filter(course_id=course_id)


# ==== QUIZ ====

class QuizListCreateView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsMentorOrReadOnly]

    def get_queryset(self):
        lesson_id = self.kwargs.get('lesson_id')
        return Quiz.objects.filter(lesson_id=lesson_id)

    def perform_create(self, serializer):
        lesson_id = self.kwargs.get('lesson_id')
        serializer.save(lesson_id=lesson_id)

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsMentorOrReadOnly]

    def get_queryset(self):
        lesson_id = self.kwargs['lesson_id']
        return Lesson.objects.filter(lesson_id=lesson_id)


# ==== ПРОГРЕСС ====
class CourseProgressListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CourseProgressUpdateView(generics.UpdateAPIView):
    serializer_class = CourseProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseProgress.objects.filter(user=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_lesson(request, course_id, lesson_id):
    user = request.user
    print(f"Пользователь: {user}, Курс: {course_id}, Урок: {lesson_id}")
    
    try:
        lesson = Lesson.objects.get(id=lesson_id, course_id=course_id)
    except Lesson.DoesNotExist:
        return Response({"error": "Lesson not found"}, status=404)

    progress, created = CourseProgress.objects.get_or_create(
        user=user,
        course=lesson.course
    )
    
    print(f"Прогресс найден: {progress}, создан: {created}")

    progress.save()
    progress.completed_lessons.add(lesson)

    all_ids = set(lesson.course.lessons.values_list('id', flat=True))
    completed_ids = set(progress.completed_lessons.values_list('id', flat=True))

    if all_ids == completed_ids:
        progress.completed_at = now()
    else:
        progress.completed_at = None

    progress.save()
    print("Урок завершён")

    return Response({"message": "Lesson marked as completed."})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_progress(request, course_id):
    user = request.user
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)

    progress, _ = CourseProgress.objects.get_or_create(user=user, course=course)
    total = course.lessons.count()
    completed = progress.completed_lessons.count()

    return Response({
        "completed_lessons": completed,
        "total_lessons": total,
        "progress_percent": round((completed / total) * 100, 2) if total else 0,
        "completed_at": progress.completed_at
    })


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


class StartChallengeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, challenge_id):
        challenge = Challenge.objects.get(id=challenge_id)
        progress, created = ChallengeProgress.objects.get_or_create(
            user=request.user,
            challenge=challenge
        )
        if not created:
            return Response({"detail": "Вы уже начали этот челлендж."}, status=400)
        return Response(ChallengeProgressSerializer(progress).data)

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