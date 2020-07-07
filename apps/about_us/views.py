from django.shortcuts import render
from . import models
from service.models import Service


def show_company(request, key):
    services = Service.objects.all()

    if key == 'profile':
        profile = models.CompanyInfo.objects.last()
        context = {
            'profile': profile,
            'services': services,
        }
        return render(request, 'about_us/company.html', context)

    if key == 'culture':
        culture = models.CompanyCulture.objects.last()
        context = {
            'culture': culture,
            'services': services,
        }
        return render(request, 'about_us/company.html', context)

    if key == 'show':
        show = models.CompanyShow.objects.last()
        context = {
            'show': show,
            'services': services,
        }
        return render(request, 'about_us/company.html', context)

    if key == 'honor':
        honor = models.Honor.objects.last()
        context = {
            'honor': honor,
            'services': services,
        }
        return render(request, 'about_us/company.html', context)

    if key == 'video':
        videos = models.Video.objects.all()
        context = {
            'videos': videos,
            'services': services,
        }
        return render(request, 'about_us/company.html', context)
