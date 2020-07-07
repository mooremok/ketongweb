from django.shortcuts import render, redirect
from .models import MessageBoard
from  service.models import Service
from django.contrib import messages

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
        services = Service.objects.all()
        context = {
            'services': services,
        }
        return render(request, 'online/messages.html', context)
