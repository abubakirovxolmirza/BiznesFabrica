from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import CustomUserSerializer, GroupSerializer
from .models import CustomUser, Group, EmailVerification, GrCode, CheckGr
from rest_framework import permissions
from .token import get_tokens_for_user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer
# Create your views here.


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        tokens = get_tokens_for_user(user)
        
        return Response(tokens)


class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
# views.py

# views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, EmailVerification
from .serializers import CustomUserSerializer

class VerifyEmailView(APIView):
    def post(self, request):
        code = request.data.get('code')
        try:
            verification = EmailVerification.objects.get(code=code)
        except EmailVerification.DoesNotExist:
            return Response({'detail': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
        
        if verification.is_expired():
            return Response({'detail': 'Verification code has expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        verification.mark_as_verified()
        user = verification.user
        user.is_active = True  # Можно активировать пользователя здесь
        user.save()

        return Response({'detail': 'Email successfully verified'}, status=status.HTTP_200_OK)

class ListGroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
    

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
    

# views.py

# views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, EmailVerification, GrCode, CheckGr
from .serializers import CustomUserSerializer, GrCodeSerializer

class GrCodeCreateView(APIView):
    def post(self, request):
        try:
            group_id = request.data.get('group_id')  # Получаем идентификатор группы из запроса
            group_instance = Group.objects.get(id=group_id)  # Получаем экземпляр группы по идентификатору
        except Group.DoesNotExist:
            return Response({'detail': 'Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        gr_code_instance = GrCode(gr_name=group_instance)
        gr_code_instance.save()  # Код будет автоматически сгенерирован при сохранении

        serializer = GrCodeSerializer(gr_code_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class CheckGrView(APIView):
    def post(self, request):
        code = request.data.get('code')

        try:
            check_instance = GrCode.objects.get(gr_code=code)
            gr_name = check_instance.gr_name.name
            gr_id = check_instance.gr_name.id
            return Response({'detail': 'Group name found', 'group_id': gr_id, 'gr_name': gr_name}, status=status.HTTP_200_OK)
        except GrCode.DoesNotExist:
            return Response({'detail': 'Invalid code'}, status=status.HTTP_404_NOT_FOUND)
