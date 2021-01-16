from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_save, pre_save


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from .models import EmailActivation
        from .signals import post_save_user_create_reciever, pre_save_email_activation
        User = settings.AUTH_USER_MODEL
        pre_save.connect(pre_save_email_activation, sender=EmailActivation)
        post_save.connect(post_save_user_create_reciever, sender=User)
