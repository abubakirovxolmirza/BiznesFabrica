# notifications/signals.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Notification
from armiya.models import Yangiliklar, Talablar, Sh_rivojlanish, Price, VAB, Tasks, TaskUsers, Balls, HistoryBalls, Buyum, Auktsion
from .middleware import CurrentUserMiddleware

def send_notification(action, instance):
    user = CurrentUserMiddleware.get_current_user()
    user_id = user.id if user else None
    user_message = f'{user_id}' if user_id else ' by an unknown user'

    Notification.objects.create(
        user=user,
        message=f'{instance.__class__.__name__} was {action}',
        user_id=user_id
    )

    # Sending notification to WebSocket
    channel_layer = get_channel_layer()
    if channel_layer:
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notify",
                "message": f'{instance.__class__.__name__} was {action}',
                "user_id": user_message
            }
        )

@receiver(post_save, sender=Yangiliklar)
@receiver(post_save, sender=Talablar)
@receiver(post_save, sender=Sh_rivojlanish)
@receiver(post_save, sender=Price)
@receiver(post_save, sender=VAB)
@receiver(post_save, sender=Tasks)
@receiver(post_save, sender=TaskUsers)
@receiver(post_save, sender=Balls)
@receiver(post_save, sender=HistoryBalls)
@receiver(post_save, sender=Buyum)
@receiver(post_save, sender=Auktsion)
def create_update_notification(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    send_notification(action, instance)

@receiver(post_delete, sender=Yangiliklar)
@receiver(post_delete, sender=Talablar)
@receiver(post_delete, sender=Sh_rivojlanish)
@receiver(post_delete, sender=Price)
@receiver(post_delete, sender=VAB)
@receiver(post_delete, sender=Tasks)
@receiver(post_delete, sender=TaskUsers)
@receiver(post_delete, sender=Balls)
@receiver(post_delete, sender=HistoryBalls)
@receiver(post_delete, sender=Buyum)
@receiver(post_delete, sender=Auktsion)
def delete_notification(sender, instance, **kwargs):
    action = 'deleted'
    send_notification(action, instance)
