from django.shortcuts import render, get_object_or_404
from .models import Service
from ad .models import SubPageBanner

def show_service(request):
    services = Service.objects.all()
    service = Service.objects.first()
    banner = get_object_or_404(SubPageBanner, id=1)
    context = {
      'services': services,
      'service': service,
    }
    return render(request, 'service/service-list.html', context)

def show_service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    services = Service.objects.all()
    context = {
        'service': service,
        'services': services,
    }
    return render(request, 'service/service-list.html', context)
    