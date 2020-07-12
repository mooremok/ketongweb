from django.urls import path
from .views import messageboard, network

app_name = 'online'

urlpatterns = [
  path('messages.html', messageboard, name='messageboard'),
  path('networks.html', network, name='network'),
]
