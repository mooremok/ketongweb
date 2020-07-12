from service.models import Service
from service.models import SpecialService

#把动态导航封装成一个字典，供其他app引入使用
def dynamic_navs(*args):
    services = Service.objects.all()
    spe_services = SpecialService.objects.all()
    context = {
        'services': services,
        'spe_services': spe_services,
    }
    return context