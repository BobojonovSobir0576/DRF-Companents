from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    """Custom Users Table"""
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    is_varified = models.BooleanField(default=False, null=True, blank=True)