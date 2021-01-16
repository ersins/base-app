from celery import shared_task
from django.core.mail import send_mail


@shared_task
def message_task(total):
    for i in range(total):
        # send_mail('subject', 'body of the message {}'.format(i), 'no-replay@klikya.net',
        #           ['ersinsenzek@yaani.com', 'ersinsenzek@yandex.com'])
        print(i)
    return "mesaj"
