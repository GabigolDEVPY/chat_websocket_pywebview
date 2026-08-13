from django.db import models


    
# Create your models here.
class Message(models.Model):
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["timestamp"]
        indexes = [models.Index(fields=["room", "timestamp"])]
    
    def __str__(self):
        return f"{self.room}, {self.user}, {self.text}"


