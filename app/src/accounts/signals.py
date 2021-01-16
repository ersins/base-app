from django.dispatch import Signal
from core.utils import random_string_generator, unique_key_generator

from .celery_task import send_activation_mail
from .models import EmailActivation


user_logged_in = Signal(providing_args=['instance', 'request'])


def pre_save_email_activation(sender, instance, *args, **kwargs):
    if not instance.activated and not instance.forced_expired:
        if not instance.key:
            instance.key = unique_key_generator(instance)


def post_save_user_create_reciever(sender, instance, created, *args, **kwargs):
    if created:
        obj = EmailActivation.objects.create(user=instance, email=instance.email)
        # obj.send_activation()
        send_activation_mail.delay(obj.id)
