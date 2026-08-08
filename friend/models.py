from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Room name: {self.name}"
    
    
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends")
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "friend"],
                name="unique_friendship"
            )
        ]


class RequestFriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_requests")
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_requests")
    accepted = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "friend"],
                name="unique_request_friend"
            )
        ]