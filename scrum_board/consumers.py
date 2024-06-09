import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'tasks'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        

    async def receive(self, text_data):
        data = json.loads(text_data)
        task = data['task']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'task_update',
                'task': task
            }
        )


    def task_update(self, event):
        # Handle task update
        self.send(text_data=json.dumps({
            'type': 'task_update',
            'task': event['task']
        }))
        
        
    def task_delete(self, event):
        # Handle task delete
        self.send(text_data=json.dumps({
            'type': 'task_delete',
            'task_id': event['task_id']
        }))