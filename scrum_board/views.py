from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


# Create your views here.
class TaskView(APIView):
    authentication_classes = [TokenAuthentication]  # Token must available
    permission_classes = [IsAuthenticated]          # User must loged in
    
    def get(self, request, format=None):
        tasks = Task.objects
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)