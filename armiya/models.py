from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# from users.models import CustomUser
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField


class Yangiliklar(models.Model):
    content = RichTextUploadingField()
    user_id = models.JSONField(default=list)
    title = models.TextField()

class Tranzaksiya(models.Model):
    from_user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='fromuser')
    to_user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='touser')
    vab = models.FloatField()

class Talablar(models.Model):
    task_id = models.ForeignKey('Tasks', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    mavzu = models.CharField(max_length=255)
    content = RichTextUploadingField()
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

class Sh_rivojlanish(models.Model):
    content = RichTextUploadingField()  

class Price(models.Model):
    vabq = models.IntegerField()
    sumq = models.FloatField()

class VAB(models.Model):
    KEY_CHOICES = [
        ('DAILY', 'DAILY'),
        ('MONTHLY', 'MONTHLY'),
        ('YEARLY', 'YEARLY'),
    ]
    date = models.DateTimeField()
    qiymat = models.FloatField()
    history = models.JSONField()
    title = models.CharField(max_length=300)
    key = models.CharField(max_length=30, choices=KEY_CHOICES)  
    is_check = models.BooleanField(default=False)

class Tasks(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    name = models.CharField(max_length=250)
    definition = models.CharField(max_length=250)
    start_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    user = models.JSONField(default=list)

    def set_score(self, user_id, ball):
        """Set or update the score for a specific user."""
        self.scores[user_id] = ball
        self.save()

    def get_score(self, user_id):
        """Get the score for a specific user."""
        return self.scores.get(user_id, 0)


class TaskUsers(models.Model):
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    users = models.ManyToManyField('users.CustomUser', related_name='armiya_tasks')
    ball = models.IntegerField(blank=True, null=True)


class Balls(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    ball = models.IntegerField()
    definition = models.CharField(max_length=250)
    tasks_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    
    
class HistoryBalls(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    ball = models.IntegerField()
    definition = models.CharField(max_length=250)
    balls_id = models.ForeignKey(Balls, on_delete=models.CASCADE)
    
    
class Buyum(models.Model):
    name = models.CharField(max_length=250)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ekb_name = models.CharField(max_length=200, blank=True, null=True)
    ekb = models.IntegerField(blank=True, null=True)
    boshlangich_narx = models.CharField(max_length=250)
    img = models.ImageField()
    buyumusers = models.ForeignKey('BuyumUsers', on_delete=models.CASCADE, blank=True, null=True)

class Auktsion(models.Model):
    vab_id = models.ForeignKey(VAB, on_delete=models.CASCADE, related_name='vab_auktsion')
    name = models.CharField(max_length=250)
    kuni = models.DateTimeField()
    yutganlar = models.CharField(max_length=100, blank=True, null=True)
    buyumlar = models.ManyToManyField(Buyum)


class BuyumUsers(models.Model):
    buyum_id = models.ForeignKey(Buyum, on_delete=models.CASCADE, related_name='buyum_user_id')
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    vab = models.IntegerField(blank=True, null=True)
