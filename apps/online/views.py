from django.shortcuts import render, redirect
from .models import MessageBoard, WechatQrCode, Network
from  service.models import Service, SpecialService
from django.contrib import messages
from ketong.navs import dynamic_navs

def messageboard(request): 
       
    if request.method == 'POST':
        title = request.POST.get('tousu-title')
        type = request.POST.get('tousu-type')
        from_to = request.POST.get('tousu-from-to')
        tel = request.POST.get('tousu-tel')
        content = request.POST.get('tousu-content')

        dicts = {
            'title': title,
            'type': type,
            'from_to': from_to,
            'tel': tel,
            'content': content,
        }

        MessageBoard.objects.create(**dicts)
        msg = '提交成功，感谢您的反馈！您也可以直接拨打客服热线：400-856-9990'
        messages.success(request, msg)
        return redirect('messages.html')
    else:
        context = dynamic_navs()
        return render(request, 'online/messages.html', context)


def qrcode(request):
    qrcode = WechatQrCode.objects.last()
    context = {
        'qrcode': qrcode,
    }
    return render(request, 'home/index.html', context)


def network(request):
    networks = Network.objects.last()
    context = {
        'networks': networks,
    }
    context.update(dynamic_navs())
    return render(request, 'online/network.html', context)
    