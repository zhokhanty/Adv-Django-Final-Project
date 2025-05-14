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

    def __str__(self):
        return f'{self.title} (Course #{self.course_id})'

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

    score = models.PositiveIntegerField(default=0)
    
    certificate_file = models.FileField(upload_to='certificates/', null=True, blank=True)

    certificate_issued = models.BooleanField(default=False)

    class Meta:
<<<<<<< HEAD
        unique_together = ('user', 'course')

=======
        unique_together = ('user', 'course')
>>>>>>> 8b36afb534a4a298b0e49ace885054b8eb8cd613
