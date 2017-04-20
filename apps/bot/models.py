from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth import get_user_model


User = get_user_model()


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages')
    date = models.DateTimeField()

    telegram_id = models.IntegerField(editable=False)  # unique per chat only

    raw = JSONField()
