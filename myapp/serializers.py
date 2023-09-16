from rest_framework import serializers
from .models import User, Visit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ("count",)
