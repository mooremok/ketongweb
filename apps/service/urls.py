from django.urls import path
from .views import show_service, show_service_detail

app_name = 'service'

urlpatterns = [
  path('service.html', show_service, name='services'),
  path('service-<int:service_id>.html', show_service_detail, name='show_service_detail'),
]