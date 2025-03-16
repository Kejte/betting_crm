
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from backend.settings import STATIC_URL, STATIC_ROOT
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path(
        'admin/', 
        admin.site.urls),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(
            url_name='schema'),
        name='swagger-ui'),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(
            url_name='schema'),
        name='redoc'),
    path(
        'api/profiles/',
        include('profiles.urls')
    ),
    path(
        'api/payments/',
        include('payments.urls')
    ),
    path(
        'api/feedback/',
        include('feedback.urls')
    )
]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)


