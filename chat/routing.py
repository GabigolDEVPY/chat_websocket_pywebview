from django.urls import path
from .consumers import consumers, status_consumers

websocket_urlpatters = [
    path("ws/chat/<str:room_name>/", consumers.ChatConsumer.as_asgi(), name="chat_websocket"),
    path("ws/status/", status_consumers.StatusConsumer.as_asgi(), name="status_websocket")
]