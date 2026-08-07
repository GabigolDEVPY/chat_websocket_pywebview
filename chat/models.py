from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Room name: {self.name}"
    
# Create your models here.
class Message(models.Model):
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.room}, {self.user}, {self.text}"

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
    
