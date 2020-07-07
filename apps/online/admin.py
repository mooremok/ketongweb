from django.contrib import admin
from . models import Network, WechatQrCode, MessageBoard
from ketong.admin import AdminBase

@admin.register(Network)
class NetWorkAdmin(AdminBase):
    pass

@admin.register(WechatQrCode)
class WechatQrCodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']

@admin.register(MessageBoard)
class MessageBoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_time', 'title', 'type', 'from_to', 'tel', 'content']
    list_display_links = ['id', 'title']
