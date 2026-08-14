from friend.models import RequestFriend, Friend, Room
from django.shortcuts import get_object_or_404
import hashlib
from django.db import transaction

class FriendService:
    @staticmethod
    def accepted_friend(request_id, user):
        with transaction.atomic():
            request_friend = get_object_or_404(RequestFriend, id=request_id, friend=user)
            room = f"{request_friend.friend.username}{user.username}"
            hash_room = hashlib.sha256(room.encode()).hexdigest()
            room = Room.objects.create(name=hash_room)
            Friend.objects.create(user=user, friend=request_friend.friend, room=room)
            Friend.objects.create(user=request_friend.friend, friend=user, room=room)
            request_friend.delete()
            
        return {"friends_requests": user.sent_requests.filter(accepted=False)}