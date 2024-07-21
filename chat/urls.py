from django.urls import path
from .views import ChatListView, ChatDetailView

urlpatterns = [
    path('chat/', ChatListView.as_view()),
    path('chat/<int:pk>/', ChatDetailView.as_view())

    ]
