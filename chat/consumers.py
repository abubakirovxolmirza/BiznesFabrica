import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat
from armiya.models import Tasks
from users.models import CustomUser

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.task_id = self.scope['url_route']['kwargs']['task_id']
        self.room_group_name = f'chat_{self.task_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = self.scope["user"].id

        # Save message to database
        task = Tasks.objects.get(id=self.task_id)
        user = CustomUser.objects.get(id=user_id)
        chat_message = Chat.objects.create(task_id=task, user_id=user, message=message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': user_id
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user_id': user_id
        }))
