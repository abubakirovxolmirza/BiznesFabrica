# middleware.py
import threading
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication

_thread_locals = threading.local()

class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = None
        if 'HTTP_AUTHORIZATION' in request.META:
            auth_header = request.META['HTTP_AUTHORIZATION']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
                try:
                    user, _ = JWTAuthentication().authenticate(request)
                except Exception:
                    user = None
        _thread_locals.user = user

    @staticmethod
    def get_current_user():
        return getattr(_thread_locals, 'user', None)
