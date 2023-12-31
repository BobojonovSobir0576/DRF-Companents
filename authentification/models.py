from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    """Custom Users Table"""
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    is_varified = models.BooleanField(default=False, null=True, blank=True)


class SmsCode(models.Model):
    """ SMS Code Table"""
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    sms_code = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)