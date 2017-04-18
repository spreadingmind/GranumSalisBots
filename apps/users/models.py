from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=255, unique=True)
    telegram_id = models.IntegerField(editable=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
