from django.db import models
from django.contrib.auth.models import User
from chat.models import Room

# Create your models here.
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "friend"],
                name="unique_request_friend"
            )
        ]