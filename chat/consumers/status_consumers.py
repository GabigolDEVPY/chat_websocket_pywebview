import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from friend.models import Friend
from chat.online import add_user, remove_user


class StatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        
        if self.user.is_anonymous:
            await self.close()
            return
        
        self.group_name = f"user_{self.user.id}"
        
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
        add_user(self.user.id)
        
        await self.notify_friends(True)
    
    
    
    
    async def disconnect(self, code):
        remove_user(self.user.id)
        await self.notify_friends(False)
        
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    
    
    
    @database_sync_to_async 
    def get_friends_ids(self):
        
        return list(
            Friend.objects.filter(user=self.user).values_list("id", flat=True)
        )




    async def notify_friends(self, online):
        friends = await self.get_friends_ids()
        
        for friend_id in friends:
            await self.channel_layer.group_send(
                f"user_{friend_id}",
                {
                    "type": "friend_status",
                    "user_id": self.user.id,
                    "online": online,
                    "user_username": self.user.username
                }
            )
        
        
        
    async def friend_status(self, event):
        await self.send(text_data=json.dumps(event)) 