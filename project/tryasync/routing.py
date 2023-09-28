from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from .consumers import WSconsumer

ws_urlpatterns = [
    path(r'ws/async/', WSconsumer.as_asgi())
]

