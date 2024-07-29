# notifications/routing.py
from django.urls import re_path
from . import consumers
from armiya import consumer
websocket_urlpatterns = [
    re_path(r'ws/yangiliklar/$', consumer.YangiliklarConsumer.as_asgi()),
    re_path(r'ws/tranzaksiya/$', consumer.TranzaksiyaConsumer.as_asgi()),
    re_path(r'ws/talablar/$', consumer.TalablarConsumer.as_asgi()),
    re_path(r'ws/sh_rivojlanish/$', consumer.ShRivojlanishConsumer.as_asgi()),
    re_path(r'ws/price/$', consumer.PriceConsumer.as_asgi()),
    re_path(r'ws/vab/$', consumer.VABConsumer.as_asgi()),
    re_path(r'ws/tasks/$', consumer.TasksConsumer.as_asgi()),
    re_path(r'ws/task_users/$', consumer.TaskUsersConsumer.as_asgi()),
    re_path(r'ws/balls/$', consumer.BallsConsumer.as_asgi()),
    re_path(r'ws/history_balls/$', consumer.HistoryBallsConsumer.as_asgi()),
    re_path(r'ws/buyum/$', consumer.BuyumConsumer.as_asgi()),
    re_path(r'ws/auktsion/$', consumer.AuktsionConsumer.as_asgi()),
    re_path(r'ws/buyum_users/$', consumer.BuyumUsersConsumer.as_asgi()),    
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]
