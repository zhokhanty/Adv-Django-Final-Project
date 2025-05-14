from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Course, CourseProgress
from .pdf_utils import generate_certificate_pdf
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets



from rest_framework import viewsets


from .models import (
    Course,
    Lesson,
    Quiz,
    CourseProgress,

)

from .serializers import (
    CourseSerializer,
    LessonSerializer,
    QuizSerializer,
    CourseProgressSerializer,
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

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsMentorOrReadOnly]   

class LessonListCreateView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsMentorOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Lesson.objects.filter(course_id=course_id)

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id')
        serializer.save(course_id=course_id)


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




class CompleteCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        try:
            progress = CourseProgress.objects.get(user=request.user, course_id=course_id)
        except CourseProgress.DoesNotExist:
            return Response({'error': 'Progress not found'}, status=404)

        total_lessons = progress.course.lessons.count()
        completed_count = progress.completed_lessons.count()

        if completed_count < total_lessons:
            return Response({'error': 'Course not fully completed'}, status=400)

        progress.completed_at = timezone.now()
        progress.score = 100  # базово, можно улучшить логику
        progress.certificate_issued = True
        progress.save()

        # Сгенерировать сертификат
        certificate_url = generate_certificate_pdf(request.user, progress.course)

        return Response({
            'message': 'Course completed',
            'score': progress.score,
            'certificate_url': request.build_absolute_uri(certificate_url)
})



class CourseCertificateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        progress = get_object_or_404(CourseProgress, user=request.user, course=course)

        if not progress.completed_at:
            return Response({"detail": "Course not completed yet."}, status=status.HTTP_403_FORBIDDEN)

        certificate_url = generate_certificate_pdf(request.user, course)
        return Response({
            "certificate_url": request.build_absolute_uri(certificate_url)
        })




def certificate_share_view(request, username, course_id):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    course = get_object_or_404(Course, id=course_id)
    
    # Путь к PDF сертификату
    pdf_url = f"/media/certificates/{user.username}_{course.id}.pdf"
    
    return render(request, "certificate_share.html", {
        "user": user,
        "course": course,
        "pdf_url": pdf_url,
    })

