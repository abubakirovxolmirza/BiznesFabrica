from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Balls, HistoryBalls

@receiver(post_save, sender=Balls)
def create_history_balls(sender, instance, **kwargs):
    if instance.status == 'Done':
        HistoryBalls.objects.create(
            status=instance.status,
            ball=instance.ball,
            definition=instance.definition,
            balls_id=instance
        )
        
        