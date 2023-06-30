from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "display_name",
            "email",
            "created_at",
            "updated_at",
            "is_student",
            "is_teacher",
        ]
