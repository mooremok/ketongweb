from django.shortcuts import render, get_object_or_404
from .models import Service, SpecialService
from ad .models import SubPageBanner

def show_service(request):
    services = Service.objects.all()
    service = Service.objects.first()
    spe_services = SpecialService.objects.all()

    context = {
      'services': services,
      'service': service,
      'spe_services': spe_services,
    }
    return render(request, 'service/service-list.html', context)

def show_service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    services = Service.objects.all()
    spe_services = SpecialService.objects.all()

    context = {
        'service': service,
        'services': services,
        'spe_services': spe_services,
    }
    return render(request, 'service/service-list.html', context)

def show_spe_service(request, spe_service_id=None):
    services = Service.objects.all()
    spe_services = SpecialService.objects.all()
    if not spe_service_id:
        service = SpecialService.objects.first()
        context = {
          'services': services,
          'spe_services': spe_services,
          'service': service,
          'is_spe': True,
        }
        return render(request, 'service/service-list.html', context)

    else:
        service = get_object_or_404(SpecialService, id=spe_service_id)
        context = {
            'services': services,
            'spe_services': spe_services,
            'service': service,
            'is_spe': True,
        }
        return render(request, 'service/service-list.html', context)

