from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, RoleUser

@receiver(post_save, sender=CustomUser)
def set_default_role(sender, instance, created, **kwargs):
    if created and not instance.role:
        default_role = RoleUser.objects.get(role='Saldat')  # Set your desired default role here
        instance.role = default_role
        instance.save()

