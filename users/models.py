from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from armiya.models import HistoryBalls, Tasks
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    
    ROLES_CHOICES = [
        ('General', 'General'),
        ('Mayor', 'Mayor'),
        ('Captain', 'Captain'),
        ('Leytenant', 'Leytenant'),
        ('Serjant', 'Serjant'),
        ('Kursant', 'Kursant'),
        ('Saldat', 'Saldat'),
        ('Bank', 'Bank'),
    ]
    username = None
    profile_photo = models.ImageField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    vab = models.ForeignKey(HistoryBalls, on_delete=models.CASCADE, blank=True, null=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True)
    reyting = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLES_CHOICES, blank=True, null=True, default="Saldat")
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True)
    permission = models.CharField(max_length=70, blank=True, null=True)
    history_tasks = models.CharField(max_length=50, blank=True, null=True)
    history_balls = models.CharField(max_length=70, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
        
    def get_role(self)-> str:
        return self.role
    
    # def __str__(self):
    #     return self.tasks
    
    def get_user_id(self):
        return self.id
        
class Group(models.Model):
    ROLES_CHOICES = [
    ('General', 'General'),
    ('Mayor', 'Mayor'),
    ('Captain', 'Captain'),
    ('Leytenant', 'Leytenant'),
    ('Serjant', 'Serjant'),
    ('Kursant', 'Kursant'),
    ('Saldat', 'Saldat'),

]
    
    name = models.CharField(max_length=200, blank=True, null=True)
    group_photo = models.ImageField()
    count = models.IntegerField(blank=True, null=True)
    admin = models.CharField(max_length=200, choices=ROLES_CHOICES, blank=True, null=True)   
    rate = models.FloatField(blank=True, null=True)
    shiori = models.CharField(max_length=200, blank=True, null=True)
    users = models.ManyToManyField('CustomUser', blank=True, null=True)     
    generate_code = models.CharField(max_length=10, null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)   

# models.py

# models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid
import random

class EmailVerification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)  # Шестизначный код подтверждения
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def generate_code(self):
        return str(random.randint(100000, 999999))  # Генерация случайного шестизначного кода

    def is_expired(self):
        expiration_time = timezone.now() - timezone.timedelta(hours=1)  # Настройте время действия по желанию
        return self.created_at < expiration_time

    def mark_as_verified(self):
        self.verified = True
        self.save()

    class Meta:
        verbose_name = 'Email Verification'
        verbose_name_plural = 'Email Verifications'
        
import random
import string  # Import string module for alphanumeric characters



# models.py

from django.db import models
from django.utils import timezone
import random
import string
# from armiya.models import Group  # Импортируем модель Group из armiya.models

class GrCode(models.Model):
    gr_name = models.ForeignKey(Group, on_delete=models.CASCADE)
    gr_code = models.CharField(max_length=10, unique=True)

    def generate_code(self):
        # Генерируем случайный код длиной 10 из букв и цифр
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    def save(self, *args, **kwargs):
        if not self.gr_code:
            self.gr_code = self.generate_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.gr_name} - {self.gr_code}'


class CheckGr(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code
