from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('duration_minutes', models.PositiveIntegerField(default=0)),
                ('tags', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='CourseProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('score', models.PositiveIntegerField(default=0)),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('certificate_issued', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('video_url', models.URLField(blank=True, null=True)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('options', models.JSONField()),
                ('correct_option', models.CharField(max_length=255)),
            ],
        ),
    ]
