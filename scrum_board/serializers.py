from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    author_username = serializers.CharField(max_length=150)
    
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'color', 'board_column', 'author', 'created_at', 'author_username']
        read_only_fields = ['author']  # Stellen Sie sicher, dass author nicht vom Client überschrieben werden können