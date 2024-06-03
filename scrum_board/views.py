from django.shortcuts import render

from rest_framework import status
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
    
    def post(self, request, format=None):
        data = request.data.copy()  # Create a mutable copy of the data
        data['author_username'] = request.user.username
        serializer = TaskSerializer(data=data)
        
        if serializer.is_valid():
            # serializer.save()
            serializer.save(author=request.user)
            print('Serialized data: ', serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)