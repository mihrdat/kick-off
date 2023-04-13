from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

swagger_urls = [
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns = [
    path("", include(swagger_urls)),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
    )
