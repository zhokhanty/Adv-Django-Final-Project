

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('challenges', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_challenges', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='challengeprogress',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='challenges.challenge'),
        ),
        migrations.AddField(
            model_name='challengeprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_progress', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='challengeprogress',
            unique_together={('user', 'challenge')},
        ),
    ]
