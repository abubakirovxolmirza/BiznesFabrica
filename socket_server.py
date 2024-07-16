import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import socketio
from django.core.serializers import serialize
from armiya.models import Tasks, Balls, HistoryBalls
import sys
sio = socketio.Server(async_mode='threading')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('Client connected', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected', sid)

@sio.event
def get_tasks(sid):
    tasks = Tasks.objects.all()
    data = serialize('json', tasks)
    sio.emit('tasks_data', data, room=sid)

@sio.event
def get_balls(sid):
    balls = Balls.objects.all()
    data = serialize('json', balls)
    sio.emit('balls_data', data, room=sid)

@sio.event
def get_history_balls(sid):
    history_balls = HistoryBalls.objects.all()
    data = serialize('json', history_balls)
    sio.emit('history_balls_data', data, room=sid)

if __name__ == '__main__':
    import os
    import django
    from django.core.management import execute_from_command_line

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()
    
    execute_from_command_line(['runserver', '127.0.0.1:8000'])
