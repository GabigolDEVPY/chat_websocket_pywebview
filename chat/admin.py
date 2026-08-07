from django.contrib import admin

from chat.models import Message, Room

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("room", "text")
    
@admin.register(Room)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    
