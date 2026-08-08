from friend.models import RequestFriend, Friend, Room
from django.shortcuts import get_object_or_404
import hashlib

class FriendService:
    @staticmethod
    def accepted_friend(request_id, user):
        request_friend = get_object_or_404(RequestFriend, id=request_id)
        request_friend.accepted = True
        request_friend.save()
        room = f"{request_friend.friend.username}{user.username}"
        hash_room = hashlib.sha256(room.encode()).hexdigest()
        room = Room.objects.create(name=hash_room)
        Friend.objects.bulk_create([
            Friend(user=user, friend=request_friend.friend, room=room),
            Friend(user=request_friend.friend, friend=user, room=room)
        ])
        request_friend.delete()
        return {"friends_requests": user.sent_requests.filter(accepted=False)}