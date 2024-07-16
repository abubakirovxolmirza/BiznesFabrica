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
class Tasks(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    name = models.CharField(max_length=250)
    definition = models.CharField(max_length=250)
    ball = models.IntegerField()
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    users = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='armiya_tasks')
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     channel_layer = get_channel_layer()
    #     async_to_sync(channel_layer.group_send)(
    #         "tasks_group",
    #         {
    #             "type": "tasks_update",
    #             "data": {
    #                 "id": self.id,
    #                 "name": self.name,
    #                 "definition": self.definition,
    #                 # "score": self.score,
    #                 "start_time": self.start_time.isoformat(),
    #                 "stop_time": self.stop_time.isoformat(),
    #                 "status": self.status,
    #             }
    #         }
    #     )

    # def delete(self, *args, **kwargs):
    #     channel_layer = get_channel_layer()
    #     async_to_sync(channel_layer.group_send)(
    #         "tasks_group",
    #         {
    #             "type": "tasks_update",
    #             "data": {"id": self.id, "deleted": True}
    #         }
    #     )
    #     super().delete(*args, **kwargs)

    
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
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     channel_layer = get_channel_layer()
    #     async_to_sync(channel_layer.group_send)(
    #         "balls_tasks_group",
    #         {
    #             "type": "balls_tasks_update",
    #             "data": {
    #                 "id": self.id,
    #                 "status": self.status,
    #                 "score": self.score,
    #                 "definition": self.definition,
    #                 "tasks_id": self.tasks_id.id,
    #             }
    #         }
    #     )

    # def delete(self, *args, **kwargs):
    #     channel_layer = get_channel_layer()
    #     async_to_sync(channel_layer.group_send)(
    #         "balls_tasks_group",
    #         {
    #             "type": "balls_tasks_update",
    #             "data": {"id": self.id, "deleted": True}
    #         }
    #     )
    #     super().delete(*args, **kwargs)
    
    
    
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

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     channel_layer = get_channel_layer()
    #     async_to_sync(channel_layer.group_send)(
    #         "history_balls_group",
    #         {
    #             "type": "history_balls_update",
    #             "data": {
    #                 "id": self.id,
    #                 "status": self.status,
    #                 "score": self.score,
    #                 "definition": self.definition,
    #                 "balls_id": self.balls_id.id,
    #             }
    #         }
    #     )

    # def delete(self, *args, **kwargs):
    #     channel_layer = get_channel_layer()
    #     async_to_sync(channel_layer.group_send)(
    #         "history_balls_group",
    #         {
    #             "type": "history_balls_update",
    #             "data": {"id": self.id, "deleted": True}
    #         }
    #     )
    #     super().delete(*args, **kwargs)
    
    
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

