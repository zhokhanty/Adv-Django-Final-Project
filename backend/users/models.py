from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Learner', 'Learner'),
        ('mentor', 'Mentor'),
        ('admin', 'Admin'),
    )
<<<<<<< HEAD
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='mentor')
=======
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Learner')
>>>>>>> a461d6aa94722e7934a74d9f31b09a7f1e1c23a6
    department = models.CharField(max_length=100, blank=True, null=True)
    is_2fa_enabled = models.BooleanField(default=False)
    otp_secret = models.CharField(max_length=32, blank=True, null=True)
