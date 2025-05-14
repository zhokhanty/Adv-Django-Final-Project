from django.db import models
from users.models import User
from django.db import models
from django.utils import timezone
from users.models import User


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
