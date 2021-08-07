# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
   url("habit_planter/", consumers.DrawConsumer.as_asgi()),
]
