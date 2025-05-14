from rest_framework import serializers
from .models import Course, Lesson, Quiz, CourseProgress

<<<<<<< HEAD
from .models import Course, Lesson, Quiz, CourseProgress


=======
>>>>>>> 8b36afb534a4a298b0e49ace885054b8eb8cd613
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'question', 'options', 'correct_option']

class LessonSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'video_url', 'order', 'quizzes']

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    creator = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'creator', 'created_at', 'updated_at', 'duration_minutes', 'tags', 'lessons']

class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = '__all__'
        read_only_fields = ('user', 'completed_at', 'certificate_issued')
