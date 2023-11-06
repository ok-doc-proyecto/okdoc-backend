from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from .consumers import MyConsumer

ws_urlpatterns = [
    path(r'functionServices/', MyConsumer.as_asgi())
]
