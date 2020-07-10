from django.urls import path
from .views import show_service, show_service_detail, show_spe_service

app_name = 'service'

urlpatterns = [
  path('service.html', show_service, name='services'),
  path('service-<int:service_id>.html', show_service_detail, name='show_service_detail'),
  path('spe-service.html', show_spe_service, name='spe_services'),
  path('spe-service-<int:spe_service_id>.html', show_spe_service, name='show_spe_services_detail'),
]