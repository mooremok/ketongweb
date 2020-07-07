from django.shortcuts import render
from ad.models import IndexBanner
from info.models import Info, News, QandA
from about_us.models import Video
from customer.models import Customer, Type
from service.models import Service


def index(request):
    #banner
    banners = IndexBanner.objects.all()[:3]
    infos = Info.objects.all()[:4]
    news = News.objects.all()[:5]
    qas = QandA.objects.all()[:5]
    videos = Video.objects.all()[:3]
    types = Type.objects.all()
    services = Service.objects.all()
    context = {
        'banners': banners,
        'infos': infos,
        'news': news,
        'qas': qas,
        'videos': videos,
        'types': types,
        'services': services,
    }
    return render(request, 'home/index.html', context)