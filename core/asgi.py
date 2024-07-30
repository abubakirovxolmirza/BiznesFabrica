import os
import logging
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from notifications.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

logger = logging.getLogger(__name__)

try:
    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        ),
    })
except Exception as e:
    logger.error(f"Error setting up ASGI application: {e}")
    raise
