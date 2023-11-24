from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import authenticate, tokens
from django.utils.encoding import smart_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.urls import reverse
from eskiz_sms import EskizSMS



class Util:

    @staticmethod
    def send(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=[data['to_email']])
        email.send()


class PasswordReset:
    @staticmethod
    def send_email(user, request):
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = tokens.PasswordResetTokenGenerator().make_token(user)

        doamin = get_current_site(request).domain

        path = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        redirect_url = settings.FRONTEND_URL + '/reset-password-complete'
        url = 'http://{}{}?redirect_url={}'.format(doamin, path, redirect_url)

        body = 'Hi! You can use the link below to reset your password on "Win corporation":\n{}'.format(url)
        data = {
            'email_subject': 'Reset your password',
            'email_body': body,
            'to_email': user.email
        }

        Util.send(data)


def send_sms(username, code_s):
    """Send SMS Function"""
    email = "Ibroxim.2001@mail.ru"
    password = "MQVib4PtVRhLOpjYcfRZRbEesmuxDWInZaEtSlaX"
    eskiz = EskizSMS(email=email, password=password)
    eskiz.send_sms(
                    username,
                    f"Sms kod {code_s}",
                    from_whom="4546",
                    callback_url=None
                    )