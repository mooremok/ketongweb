from django.contrib import admin
from ketong.admin import AdminBase
from .models import CompanyInfo, CompanyShow, CompanyCulture, Honor, Video
# Register your models here.


@admin.register(CompanyInfo)
class CompanyInfoAdmin(AdminBase):
    list_display = ['title', 'description', 'image']


@admin.register(CompanyShow)
class CompanyShowAdmin(AdminBase):
    list_display = ['title', 'description', 'image']

@admin.register(CompanyCulture)
class CompanyCultureAdmin(AdminBase):
    list_display = ['title', 'description', 'image']

@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    list_display_links = ['title']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'video']
    list_display_links = ['title']