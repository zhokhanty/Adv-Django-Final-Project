from django.db import models
from users.models import User
from django.db import models
from django.utils import timezone
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration_minutes = models.PositiveIntegerField(default=0)
    tags = models.JSONField(default=list)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField()

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    options = models.JSONField()  # пример: ["a", "b", "c"]
    correct_option = models.CharField(max_length=255)

class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_lessons = models.ManyToManyField(Lesson, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)



# models.py
class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenges')
    days = models.PositiveIntegerField(choices=[(7, '7 дней'), (30, '30 дней')])
    tags = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

class ChallengeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenge_progress')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='progress')
    current_day = models.PositiveIntegerField(default=1)
    completed_days = models.JSONField(default=list)  # Пример: [1, 2, 3]
    started_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'challenge')
