from django.urls import path
from .consumers import NotificationConsumer

websocket_urlpatters = [
    path("ws/notification/", NotificationConsumer.as_asgi(), name="notification_websocket")
]