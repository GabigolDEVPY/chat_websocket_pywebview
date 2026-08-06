from django.urls import path
from . import consumers

websocket_urlpatters = [
    path("ws/chat/<str:room_name>/", consumers.ChatConsumer.as_asgi(), name="chat_websocket")
]