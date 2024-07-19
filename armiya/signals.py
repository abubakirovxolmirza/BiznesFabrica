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
        
        
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Price, VAB

@receiver(post_save, sender=Price)
def update_vab(sender, instance, **kwargs):
    try:
        # Get the most recent VAB entry
        latest_vab = VAB.objects.latest('date')
    except VAB.DoesNotExist:
        # If no VAB entry exists, create one
        latest_vab = VAB.objects.create(date=timezone.now(), value=instance.sumq, history=[])

    # Update the history and value
    new_history = latest_vab.history
    new_history.append({
        "timestamp": timezone.now().isoformat(),
        "value": instance.sumq
    })

    # Update the latest VAB entry
    latest_vab.value = instance.sumq
    latest_vab.history = new_history
    latest_vab.date = timezone.now()
    latest_vab.save()



