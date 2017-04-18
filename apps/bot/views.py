from django.views.generic import View
from django.http import HttpResponse


class WebhookView(View):
    def post(self, request):
        print(request)
        return HttpResponse()
