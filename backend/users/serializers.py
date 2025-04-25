from .utils import generate_otp_secret
from .models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.otp_secret = generate_otp_secret()
        user.save()
        return user
