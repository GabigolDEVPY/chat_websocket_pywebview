from django.contrib import admin
from .models import Friend, RequestFriend, Room

# Register your models here.
@admin.register(Friend)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", "room")
    
@admin.register(RequestFriend)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", "accepted")
    
    
@admin.register(Room)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
        