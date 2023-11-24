from django.urls import re_path, path

from chat.consumers import (
    ChatConsumer
)

from notification.consumers import (
    NotificationConsumer
)

websocket_urlpatterns = [
    path('ws/chat/<int:room_name>/', ChatConsumer.as_asgi()),
    path('ws/notification/', NotificationConsumer.as_asgi())
]