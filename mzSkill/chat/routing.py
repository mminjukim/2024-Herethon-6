from django.urls import re_path
from . import consumers

# 라우팅 설정

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<username>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
