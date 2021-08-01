"""
ASGI config for cocktailapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from cocktail.routing import ws_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocktailapi.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websoket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})