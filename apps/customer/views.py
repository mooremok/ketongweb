from django.shortcuts import render
from . models import Customer, Type
from service.models import Service

def customers(request):
    customers = Customer.objects.all()
    types = Type.objects.all()
    services = Service.objects.all()
    context = {
        'services': services,
        'customers': customers,
        'types': types,
    }
    return render(request, 'customer/customer.html', context)