from django.shortcuts import render
from . models import Customer, Type
from service.models import Service, SpecialService

def customers(request):
    customers = Customer.objects.all()
    types = Type.objects.all()
    services = Service.objects.all()
    spe_services = SpecialService.objects.all()
    context = {
        'services': services,
        'customers': customers,
        'types': types,
        'spe_services': spe_services,
    }
    return render(request, 'customer/customer.html', context)