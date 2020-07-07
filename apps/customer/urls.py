from django.urls import path
from .views import customers

app_name = 'customer'

urlpatterns = [
  path('customers.html', customers, name='customers'),
]