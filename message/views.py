from django.shortcuts import render

from main.models import User, Mes
# Create your views here.


def index(request, checkcode):
    try:
        user = User.objects.get(checkcode=checkcode)
        mesr = Mes.objects.filter(taru=user.name)
        mesp = Mes.objects.filter(fromu=user.name)
        context = {'checkcode': checkcode, 'Mesr': mesr, 'Mesp': mesp}
        return render(request, 'message/Mes_Box.html', context)
    except:
        context = {'Response': '无消息', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)


def mes(request, checkcode):
    try:
        User.objects.get(checkcode=checkcode)
        context = {'checkcode': checkcode}
        return render(request, 'post/post_m.html', context)
    except:
        context = {'Response': '无发件许可', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)




