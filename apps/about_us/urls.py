from django.urls import path
from . import views

app_name = 'about_us'

urlpatterns = [
  path('company-<str:key>.html',  views.show_company, name='about_us'),
]