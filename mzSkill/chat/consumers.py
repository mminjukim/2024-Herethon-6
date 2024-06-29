import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
from django.contrib.auth.models import User

# 웹소켓 받아주는 통신형 파일
# 채팅창에 들어가면 그 접속된 URL에 대한 웹 소켓을 받아주는 consumer가 필요하다.
# 모든 consumer 인스턴스는 자동으로 유일한 channel name을 생성하기 때문에, 서로 channel layer를 통해 통신할 수 있다.

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = f'chat_{self.room_name}'

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

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['user']
        
        # Find the receiver user
        receiver = await sync_to_async(User.objects.get)(username=self.room_name)
        
        # Save the message to the database
        await sync_to_async(Message.objects.create)(
            sender=sender,
            receiver=receiver,
            content=message
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))


