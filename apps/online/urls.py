from django.urls import path
from .views import messageboard

app_name = 'online'

urlpatterns = [
  path('messages.html', messageboard, name='messageboard'),
]
