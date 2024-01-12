"""
ASGI config for okdoc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from tryasync.routing import ws_urlpatterns as tryasync_urlpatterns
from functionServices.routing import ws_urlpatterns as functionServices_urlpatterns

from   channels.routing import URLRouter
from   channels.routing import ProtocolTypeRouter
from   channels.auth    import AuthMiddlewareStack
from   django.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'okdoc.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(tryasync_urlpatterns +
                                               functionServices_urlpatterns))

})
