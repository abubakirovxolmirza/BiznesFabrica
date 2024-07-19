from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# from users.models import CustomUser
# Create your models here.

from ckeditor_uploader.fields import RichTextUploadingField    
class Yangiliklar(models.Model):
    content = RichTextUploadingField()
    
class Talablar(models.Model):
    content = RichTextUploadingField()
    
class Sh_rivojlanish(models.Model):
    content = RichTextUploadingField()  

class Price(models.Model):
    vabq = models.IntegerField()
    sumq = models.FloatField()

from django.db import models

class VAB(models.Model):
    date = models.DateTimeField()
    value = models.FloatField()
    history = models.JSONField(default=list)  # Ensure this is the correct JSONField

    class Meta:
        ordering = ['-date']



class Tasks(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    name = models.CharField(max_length=250)
    definition = models.CharField(max_length=250)
    # ball = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    # users = models.ManyToManyField('users.CustomUser', related_name='armiya_tasks')
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)


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
    ekb_name = models.CharField(max_length=200)
    ekb = models.IntegerField()
    boshlangich_narx = models.CharField(max_length=250)
    
    
class Auktsion(models.Model):
    name = models.CharField(max_length=250)
    kuni = models.DateField()
    yutganlar = models.CharField(max_length=100)
    buyumlar = models.ForeignKey(Buyum, on_delete=models.CASCADE)

