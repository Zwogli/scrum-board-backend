from django.urls import path
from scrum_board import consumers

websocket_urlpatterns = [
    path(r'ws/task/$', consumers.TaskConsumer.as_asgi()),
]