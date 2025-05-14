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
<<<<<<< HEAD
    score = models.PositiveIntegerField(default=0)
    certificate_issued = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'course')

=======

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration_days = models.PositiveIntegerField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_challenges', null=True)

    def add_user(self, user):
        if ChallengeProgress.objects.filter(challenge=self, user=user).exists():
            return None

        progress = ChallengeProgress.objects.create(
            user=user,
            challenge=self,
            completed_days=[],
        )
        return progress

class ChallengeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenge_progress')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='progress')
    current_day = models.PositiveIntegerField(default=1)
    completed_days = models.JSONField(default=list)  # Пример: [1, 2, 3]
    started_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'challenge')
>>>>>>> a461d6aa94722e7934a74d9f31b09a7f1e1c23a6
