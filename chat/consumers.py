import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        print(self.room_name)
        self.room_group_name = f"chat_{self.room_name}"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        history = await self.load_messages(self.room_name)
        print(history)
        await self.send(text_data=json.dumps({
            "type": "history",
            "messages": history
        }))
        
        
        
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = self.scope["user"].username
        
        await self.save_message(self.room_name, message, username)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username
            }
        )
        
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "type": "message",
            "message": event["message"],
            "username": event["username"]
        }))
    
    
    @database_sync_to_async
    def save_message(self, room_name, message, user):
        Message.objects.create(
            user = user,
            room = room_name,
            text = message
        )
        return

    @database_sync_to_async
    def load_messages(self, room, limit=50):
        from django.db import transaction
        with transaction.atomic():
            messages = Message.objects.filter(room=room)[:limit]
        
        return [
            {"user": m.user, "room": m.room, "text": m.text}  for m in messages  
        ]