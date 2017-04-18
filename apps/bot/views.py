from django.http import HttpResponse
from rest_framework.views import APIView


class WebhookView(APIView):
    def post(self, request):
        print(request.data)
        return HttpResponse()
