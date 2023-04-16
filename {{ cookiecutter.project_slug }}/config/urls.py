from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("config.swagger.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path("__debug__/", include("debug_toolbar.urls")),
            *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        ]
    )
