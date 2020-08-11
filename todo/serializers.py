from rest_framework import serializers
from .models import Task, Step
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['task', 'created_at', 'modified_date', 'segment', 'steps', 'owner']
