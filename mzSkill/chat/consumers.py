import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from .models import Message
from django.contrib.auth.models import User

# 웹소켓 받아주는 통신형 파일
# 채팅창에 들어가면 그 접속된 URL에 대한 웹 소켓을 받아주는 consumer가 필요하다.
# 모든 consumer 인스턴스는 자동으로 유일한 channel name을 생성하기 때문에, 서로 channel layer를 통해 통신할 수 있다.

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self): # username -> room_name
        self.receiver_username = self.scope['url_route']['kwargs']['username']
        self.room_name = f"chat_{self.scope['user'].username}_{self.receiver_username}"
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
        sender_username = self.scope['user'].username # 수정된 부분
        
        sender = await sync_to_async(User.objects.get)(username=sender_username)
        receiver = await sync_to_async(User.objects.get)(username=self.receiver_username)
        
        # db에 메세지 저장
        chat_message = await self.save_message(sender, receiver, message)
        
        timestamp = chat_message.timestamp.strftime('%Y-%m-%d %H:%M:%S')


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                'timestamp': timestamp
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'timestamp': timestamp
        }))

    @database_sync_to_async
    def save_message(self, sender, receiver, message):
        return Message.objects.create(sender=sender, receiver=receiver, content=message)