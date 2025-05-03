from rest_framework import generics, permissions
from .models import Course, Lesson, Quiz, CourseProgress
from .serializers import CourseSerializer, LessonSerializer, QuizSerializer, CourseProgressSerializer
from users.permissions import IsMentorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from .models import Lesson, Quiz
from .serializers import LessonSerializer, QuizSerializer
from rest_framework.permissions import IsAuthenticated

# ==== LESSON ====

class LessonListCreateView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsMentorOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Lesson.objects.filter(course_id=course_id)

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id')
        serializer.save(course_id=course_id)

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsMentorOrReadOnly]


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
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsMentorOrReadOnly]


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
