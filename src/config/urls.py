from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from config.swaggers.merchant import MerchantSpectacularAPIView, MerchantSpectacularSwaggerView
from config.swaggers.client import ClientSpectacularSwaggerView, ClientSpectacularAPIView
from config.swaggers.admin import AdminSpectacularAPIView, AdminSpectacularSwaggerView

urlpatterns = [
    # path('', TemplateView.as_view(
    #     template_name='index.html'
    # )),
    path('openapi.json', SpectacularAPIView.as_view(), name='schema'),
    path('admin_openapi.json', AdminSpectacularAPIView.as_view(), name='admin_schema'),
    path('client_openapi.json', ClientSpectacularAPIView.as_view(), name='client_schema'),
    path('merchant_openapi.json', MerchantSpectacularAPIView.as_view(), name='merchant_schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swaggers-ui'),
    path('swagger/admin/', AdminSpectacularSwaggerView.as_view(url_name='admin_schema'), name='swaggers-ui-admin'),
    path('swagger/client/', ClientSpectacularSwaggerView.as_view(url_name='client_schema'), name='swaggers-ui-client'),
    path('swagger/merchant/', MerchantSpectacularSwaggerView.as_view(url_name='merchant_schema'), name='swaggers-ui-merchant'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ]
