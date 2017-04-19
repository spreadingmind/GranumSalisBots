from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

User = get_user_model()


class TelegramAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        try:
            telegram_id = request.data['message']['from']['id']
            username = request.data['message']['from']['username']
        except KeyError:
            raise PermissionDenied

        user, _ = User.objects.get_or_create(telegram_id=telegram_id, defaults={
            'username': username
        })

        if user.username != username:
            user.username = username
            user.save()

        return user, None
