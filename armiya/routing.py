# your_app_name/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/yangiliklar/$', consumers.YangiliklarConsumer.as_asgi()),
    re_path(r'ws/tranzaksiya/$', consumers.TranzaksiyaConsumer.as_asgi()),
    re_path(r'ws/talablar/$', consumers.TalablarConsumer.as_asgi()),
    re_path(r'ws/sh_rivojlanish/$', consumers.ShRivojlanishConsumer.as_asgi()),
    re_path(r'ws/price/$', consumers.PriceConsumer.as_asgi()),
    re_path(r'ws/vab/$', consumers.VABConsumer.as_asgi()),
    re_path(r'ws/tasks/$', consumers.TasksConsumer.as_asgi()),
    re_path(r'ws/task_users/$', consumers.TaskUsersConsumer.as_asgi()),
    re_path(r'ws/balls/$', consumers.BallsConsumer.as_asgi()),
    re_path(r'ws/history_balls/$', consumers.HistoryBallsConsumer.as_asgi()),
    re_path(r'ws/buyum/$', consumers.BuyumConsumer.as_asgi()),
    re_path(r'ws/auktsion/$', consumers.AuktsionConsumer.as_asgi()),
    re_path(r'ws/buyum_users/$', consumers.BuyumUsersConsumer.as_asgi()),
]
