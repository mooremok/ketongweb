from django.shortcuts import render
from . import models
from service.models import Service, SpecialService
from ketong.navs import dynamic_navs


def show_company(request, key):

    if key == 'profile':
        profile = models.CompanyInfo.objects.last()
        context = {
            'profile': profile,
        }
        context.update(dynamic_navs())
        return render(request, 'about_us/company.html', context)

    if key == 'culture':
        culture = models.CompanyCulture.objects.last()
        context = {
            'culture': culture,
        }
        context.update(dynamic_navs())
        return render(request, 'about_us/company.html', context)

    if key == 'show':
        show = models.CompanyShow.objects.last()
        context = {
            'show': show,
        }
        context.update(dynamic_navs())
        return render(request, 'about_us/company.html', context)

    if key == 'honor':
        honor = models.Honor.objects.last()
        context = {
            'honor': honor,
        }
        context.update(dynamic_navs())
        return render(request, 'about_us/company.html', context)

    if key == 'video':
        videos = models.Video.objects.all()
        context = {
            'videos': videos,
        }
        context.update(dynamic_navs())
        return render(request, 'about_us/company.html', context)