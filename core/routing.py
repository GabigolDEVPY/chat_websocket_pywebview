
from django.urls import path
from notification.consumers import NotificationConsumer
from chat.consumers import consumers, status_consumers

websocket_urlpatters = [
    path("ws/notification/", NotificationConsumer.as_asgi(), name="notification_websocket"),
    path("ws/chat/<str:room_name>/", consumers.ChatConsumer.as_asgi(), name="chat_websocket"),
    path("ws/status/", status_consumers.StatusConsumer.as_asgi(), name="status_websocket")
]


