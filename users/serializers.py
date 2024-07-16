from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, EmailVerification, Group
  
from django.core.mail import send_mail
from django.template.loader import render_to_string

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)

        # Generate and save email verification code
        verification_code = EmailVerification(user=user)
        verification_code.code = verification_code.generate_code()
        verification_code.save()

        # Send verification email
        self.send_verification_email(user.email, verification_code.code)

        return user

    def send_verification_email(self, to_email, code):
        subject = 'Email Verification Code'
        message = f'Your verification code is: {code}'
        send_mail(subject, message, None, [to_email], fail_silently=False)
    

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': user.get_role(),
            'user_id': user.id,
        }
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
# serializers.py

from rest_framework import serializers
from .models import CustomUser, GrCode, CheckGr

class GrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrCode
        fields = ('id', 'gr_name', 'gr_code')
        read_only_fields = ('gr_code',)  # gr_code будет сгенерирован автоматически

class CheckGrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckGr
        fields = ('id', 'code')
