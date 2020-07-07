from django.contrib import admin
from ketong.admin import AdminBase
from .models import Info, News, QandA
# Register your models here.

@admin.register(Info)
class InfoAdmin(AdminBase):
    list_display = ['title', 'created_time', 'image']
    list_display_links = ['title']

@admin.register(News)
class NewsAdmin(AdminBase):
    pass

@admin.register(QandA)
class QandAAdmin(AdminBase):
    pass