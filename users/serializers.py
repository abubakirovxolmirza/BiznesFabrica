from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, EmailVerification, Group, RoleUser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import email.utils
from django.core.mail import send_mail
from django.template.loader import render_to_string
import uuid  # Import uuid module

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'profile_photo', 'phone_number', 'age', 'vab', 'tasks', 'reyting', 'status', 'role', 'group_id', 'permission', 'history_tasks', 'history_balls', 'password')
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
        sender_email = "info@biznes-armiya.uz"
        receiver_email = to_email
        subject = "Email Verification"
        smtp_server = "server2.ahost.uz"
        smtp_port = 465
        smtp_username = "info@biznes-armiya.uz"
        smtp_password = "AS2zzCfKCCHMG9n"

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg['Message-ID'] = f"<{uuid.uuid4()}@biznes-armiya.uz>"

        # HTML part
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Email Confirmation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }}
                .header {{
                    text-align: center;
                    padding: 20px;
                }}
                .header img {{
                    max-width: 100%;
                    height: auto;
                }}
                .content {{
                    text-align: center;
                    padding: 20px;
                }}
                .content h1 {{
                    font-size: 24px;
                    color: #333333;
                }}
                .code {{
                    font-size: 32px;
                    font-weight: bold;
                    color: #333333;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    padding: 20px;
                    color: #777777;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <img src="cid:email_logo" alt="Email Verification">
                </div>
                <div class="header">
                    <img src="cid:email_image" alt="Email Verification">
                </div>
                <div class="content">
                    <h1>Salom!</h1>
                    <p>Onlayn formangiz uchun tasdiqlash kodi:</p>
                    <div class="code">{code}</div>
                    <p>Barcha qilishingiz kerak bo'lgan narsa tasdiqlash kodini nusxalash va
          uni elektron pochta tasdiqlash jarayonini yakunlash uchun formangizga
          joylashtirish.</p>
                </div>
                <div class="footer">
                    <p>&copy; 2024 biznes-armiya.uz. Barcha huquqlar himoyalangan.</p>
                </div>
            </div>
        </body>
        </html>
        """

        msg.attach(MIMEText(html, 'html'))

        # Attach the image
        with open("email-vector.png", 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<email_image>')
            msg.attach(img)

        with open("email-logo.png", 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<email_logo>')
            msg.attach(img)

        # Send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
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
            'role': user.role.id,
            'user_id': user.id,
        }
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class RoleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUser
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
