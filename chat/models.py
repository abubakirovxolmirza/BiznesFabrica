from django.db import models
from armiya.models import Tasks
from users.models import CustomUser
# Create your models here.
class Chat(models.Model):
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
