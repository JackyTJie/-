from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import User, Info, Com
# Create your views here.


def detail(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
        info = Info.objects.get(id=int(tid))
        com = Com.objects.filter(tarInfo=int(tid))
        if info.hide == 'True':
            aut = 'revealed'
        else:
            aut = info.fromu
        context = {'author': aut, 'title': info.title, 'text': info.text, 'img': info.picture, 'com': com, 'tid': tid,
                   'user': user}
        return render(request, 'detail/detail_page.html', context)
    except:
        context = {'Response': 'Please login', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)


def star(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
        user.star = user.star + '/' + tid
        user.save()
        return HttpResponseRedirect('/detail/' + checkcode + '/' + tid)
    except:
        context = {'Response': 'Please login', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)
