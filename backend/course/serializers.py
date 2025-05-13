from rest_framework import serializers
from .models import Course, Lesson, Quiz, CourseProgress, Challenge, ChallengeProgress

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
    completed_lessons = serializers.PrimaryKeyRelatedField(many=True, queryset=Lesson.objects.all())

    class Meta:
        model = CourseProgress
        fields = ['id', 'user', 'course', 'completed_lessons', 'completed_at']
        read_only_fields = ['user']

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
        read_only_fields = ('creator', 'created_at')

    def create(self, validated_data):
        validated_data.pop('creator', None)
        return super().create(validated_data)

class ChallengeProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeProgress
        fields = '__all__'
        read_only_fields = ('user', 'started_at', 'completed_at')