from django.shortcuts import render
from . models import Customer, Type
from service.models import Service, SpecialService
from ketong.navs import dynamic_navs


def customers(request):
    customers = Customer.objects.all()
    types = Type.objects.all()
    context = {
        'customers': customers,
        'types': types,
    }
    context.update(dynamic_navs())
    return render(request, 'customer/customer.html', context)