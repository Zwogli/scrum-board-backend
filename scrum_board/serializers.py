from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'color', 'board_column', 'author', 'created_at']
        read_only_fields = ['author']  # Stellen Sie sicher, dass author nicht vom Client überschrieben werden können