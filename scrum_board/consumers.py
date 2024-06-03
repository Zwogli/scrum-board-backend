import json
from channels.generic.websocket import WebsocketConsumer

class TaskConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass
    
    def inform_clients(self, event):
        # Send a message to the WebSocket
        self.send(text_data=json.dumps({
            'message': event['message']
        }))