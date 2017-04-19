from django.http import HttpResponse
from rest_framework.views import APIView

from .auth import TelegramAuthentication


class WebhookView(APIView):
    authentication_classes = [TelegramAuthentication]

    def post(self, request):
        print(request.data)
        print(request.user)
        return HttpResponse()
