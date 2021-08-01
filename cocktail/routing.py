from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from .consumers import CocktailConsumer

ws_urlpatterns = [
    path('ws/cocktail/',CocktailConsumer.as_asgi())
]

#application = ProtocolTypeRouter({
#    "websocket": AllowedHostsOriginValidator(
#        AuthMiddlewareStack(
#            #URLRouter([ ]) #empty for now because we don't have a consumer yet
#        )
#    ),
#})
