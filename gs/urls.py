from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin

admin.site.site_title = admin.site.site_header = admin.site.index_title = 'Bot Admin'

urlpatterns = [
    url(r'^api/', include('gs.api', namespace='api')),
    url(r'^', admin.site.urls),

] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
