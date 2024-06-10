from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


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
            serializer.save(author=request.user)
            print('Serialized data: ', serializer.data)
            
            # Nachricht über den WebSocket senden
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'tasks',
                {
                    'type': 'task_update',
                    'task': serializer.data
                }
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            # Nachricht über den WebSocket senden
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'tasks',
                {
                    'type': 'task_update',
                    'task': serializer.data
                }
            )
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        
        # Nachricht über den WebSocket senden
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'tasks',
            {
                'type': 'task_delete',
                'task_id': pk
            }
        )
        
        return Response(status=status.HTTP_204_NO_CONTENT)