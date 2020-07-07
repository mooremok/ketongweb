from django.contrib import admin

class AdminBase(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']