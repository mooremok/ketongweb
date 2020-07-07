from django.contrib import admin
from .models import Service, SpecialService, KeeperService
from ketong.admin import AdminBase

@admin.register(Service)
class ServiceAdmin(AdminBase):
    pass

@admin.register(SpecialService)
class SpecialServiceAdmin(AdminBase):
    pass

@admin.register(KeeperService)
class KeeperServiceAdmin(AdminBase):
    pass
