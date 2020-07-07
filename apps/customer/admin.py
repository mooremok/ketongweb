from django.contrib import admin
from .models import Type, Customer

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'description', 'customer_logo']
    list_display_links = ['id', 'title']
