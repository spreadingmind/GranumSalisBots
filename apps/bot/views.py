from django.http import HttpResponse
from rest_framework.views import APIView

from datetime import datetime

from .auth import TelegramAuthentication
from .models import Message


class WebhookView(APIView):
    authentication_classes = [TelegramAuthentication]

    def post(self, request):
        msg = Message.objects.create(
            user=request.user,
            raw=request.data['message'],
            telegram_id=request.data['message']['message_id'],
            date=datetime.fromtimestamp(request.data['message']['date']),
        )
        print(msg)
        return HttpResponse()
