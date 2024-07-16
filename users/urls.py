from django.urls import path
from .views import GrCodeCreateView, CheckGrView, RegisterUserView, ListUsersView, CustomUserDetailView, CustomTokenObtainPairView, VerifyEmailView, ListGroupView, GroupDetailView

urlpatterns = [
    path('register', RegisterUserView.as_view()),
    path('users', ListUsersView.as_view()),
    path('users/<int:pk>', CustomUserDetailView.as_view()),
    path('login', CustomTokenObtainPairView.as_view()),
    path('verify-email', VerifyEmailView.as_view(), name='verify-email'),
    path('group', ListGroupView.as_view()),
    path('group/<int:pk>', GroupDetailView.as_view()),
    path('create-gr-code/', GrCodeCreateView.as_view(), name='create-gr-code'),
    path('check-gr/', CheckGrView.as_view(), name='check-gr'),
]
