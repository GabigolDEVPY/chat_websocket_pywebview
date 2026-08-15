from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f"notification_{self.scope['user'].id}"
        print(self.scope['user'], "sala", self.room_name)
        
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        
        await self.accept()
    
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )
        
    async def friend_request_notification(self, event):
        print("cheguei no friend request consumer")
        payload = event["payload"]
        await self.send(text_data=json.dumps({
                "type": "friend_request_notification", 
                "id": payload["id"], 
                "user_id": payload["user_id"], 
                "username": payload["username"]
            }))
    