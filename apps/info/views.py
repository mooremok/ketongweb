from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Info, QandA
from ketong.navs import dynamic_navs

def info(request, info_id=None):
    infos = Info.objects.all()
    if not info_id:
        paginator = Paginator(infos, 15)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        context = {
          'infos': infos,
          'page_obj': page_obj,
          'paginator': paginator,
          'is_paginated': True,
          'is_infos': True,
        }
        context.update(dynamic_navs())
        return render(request, 'info/company-info.html', context)
    else:
        info = get_object_or_404(Info, id=info_id)
        context = {
          'info': info,
          'is_info': True,
        }
        context.update(dynamic_navs())
        return render(request, 'info/company-info.html', context)


def news(request, news_id=None):
    news = News.objects.all()
    if not news_id:
        paginator = Paginator(news, 15)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        context = {
          'is_paginated': True,
          'paginator': paginator,
          'page_obj': page_obj,
          'is_news': True,
        }
        context.update(dynamic_navs())
        return render(request, 'info/news.html', context)
    else:
        new = get_object_or_404(News, id=news_id)
        context = {
          'is_new': True,
          'new': new,
        }
        context.update(dynamic_navs())
        return render(request, 'info/news.html', context)

def qas(request, q_id=None):
    qas = QandA.objects.all()
    if not q_id:
        paginator = Paginator(qas, 15)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        context = {
          'paginator': paginator,
          'page_obj': page_obj,
          'is_paginated': True,
          'is_qas': True,
        }
        context.update(dynamic_navs())
        return render(request, 'info/qanda.html', context)
    else:
        qa = get_object_or_404(QandA, id=q_id)
        context = {
          'is_qa': True,
          'qa': qa,
        }
        context.update(dynamic_navs())
        return render(request, 'info/qanda.html', context)