from rest_framework import serializers
from .models import Challenge, ChallengeProgress

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