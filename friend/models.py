from django.db import models

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
    
