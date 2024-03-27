from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


# Create your views here.
class TaskView(APIView):
    def get(self, request, format=None):
        tasks = Task.objects
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)