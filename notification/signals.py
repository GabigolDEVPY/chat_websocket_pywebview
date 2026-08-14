from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from friend.models import RequestFriend
print("signals importado")

@receiver(post_save, sender=RequestFriend)
def friend_request_created(sender, instance, created, **kwargs):
    if not created:
        return
    
    channel_layer = get_channel_layer()
    print("chamdno create friend")
    async_to_sync(channel_layer.group_send)(
        f"notification_{instance.friend.id}",
        {
            "type": "friend_request.notification",
            "payload": {
                "id": instance.id,
                "user_id": instance.user.id,
                "username": instance.user.username
            }
        }
    )
    