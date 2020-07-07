from django.contrib import admin
from .models import IndexBanner, SubPageBanner


@admin.register(IndexBanner)
class IndexBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'image']
    list_display_links = ['id', 'title']


@admin.register(SubPageBanner)
class SubPageBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'image']
    list_display_links = ['id', 'title']
