from django.urls import path, include

urlpatterns = [
    path('admin/', include('api.admin.urls')),
    path('merchant/', include('api.merchant.urls')),
    path('client/', include('api.client.urls')),
]
