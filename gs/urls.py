from django.conf import settings
from django.conf.urls import url, include, static
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib import admin

from apps.bot.views import WebhookView

admin.site.site_title = admin.site.site_header = admin.site.index_title = 'Bot Admin'

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include('gs.api', namespace='api')),
    url(f'^webhook/{settings.SECRET_WEBHOOK_PATH}/', csrf_exempt(WebhookView.as_view())),
    url(r'django_admin/^', admin.site.urls),

] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
