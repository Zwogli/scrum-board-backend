import json
from channels.generic.websocket import WebsocketConsumer

class TaskConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Hier kannst du die empfangene Nachricht verarbeiten und auf andere Clients senden
        self.send(text_data=json.dumps({
            'message': message
        }))