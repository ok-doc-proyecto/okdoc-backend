"""
ASGI config for okdoc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'okdoc.settings')
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from tryasync.routing import ws_urlpatterns



application = ProtocolTypeRouter({
   'http' : get_asgi_application(), 
   'websocket' : AuthMiddlewareStack(URLRouter(ws_urlpatterns))

})
