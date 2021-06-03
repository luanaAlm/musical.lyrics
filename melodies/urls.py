from django.contrib import admin
from django.urls import path, include

# media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
]
# media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
