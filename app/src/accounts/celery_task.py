from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.urls import reverse

from .models import EmailActivation


@shared_task
def send_activation_mail(email_activation_id):
    """
    Kullanıcı aktivasyonu için kullanılan celery task fonksiyonu post_save_user_create_reciever signals tarafından kullanılır
    :param email_activation_id:
    :return:
    """
    email_activation_obj = EmailActivation.objects.get(id=email_activation_id)
    print(f'Buraya geldi 1...........')

    if not email_activation_obj.activated and not email_activation_obj.forced_expired:
        print(f'Buraya geldi 2...........')
        if email_activation_obj.key:
            print(f'Buraya geldi 3...........')
            base_url = getattr(settings, 'BASE_URL', 'https://www.ersins.com')
            key_path = reverse("account:email-activate", kwargs={'key': email_activation_obj.key})  # use reverse
            path = "{base}{path}".format(base=base_url, path=key_path)
            context = {
                'path': path,
                'email': email_activation_obj.email
            }
            txt_ = get_template("registration/emails/verify.txt").render(context)
            # TODO email template düzenlenecek
            html_ = get_template("registration/emails/verify.html").render(context)
            subject = '1-Click Email Verification'
            subject = '1-Click Email Verification'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email_activation_obj.email]
            sent_mail = send_mail(
                subject,
                txt_,
                from_email,
                recipient_list,
                html_message=html_,
                fail_silently=False,
            )
             # return sent_mail
     # return False
