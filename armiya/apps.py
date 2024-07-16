from django.apps import AppConfig


class ArmiyaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'armiya'

    def ready(self):
        import armiya.signals