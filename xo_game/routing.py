from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/(?P<gameid>\w+)/$',
            consumers.GameConsumers.as_asgi())
]
