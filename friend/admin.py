from django.contrib import admin
from .models import Friend, RequestFriend

# Register your models here.
@admin.register(Friend)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", "room")
    
@admin.register(RequestFriend)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", "accepted")