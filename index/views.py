from django.shortcuts import render

from main.models import User, Com
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def red(request):
    return HttpResponseRedirect('/main/visitor/1')
    # context = {'Response': 'Welcome to BBQ', 'url': '/main/visitor/1'}
    # return render(request, 'Res.html', context)


def com(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
        com = Com()
        try:
            lc = Com.objects.last()
            cid = lc.id + 1
        except:
            cid = 1
        com.id = cid
        com.idstr = str(cid)
        com.tarInfo = int(tid)
        com.text = request.POST['co']
        com.thumb = 0
        com.fromu = user.name
        com.save()
        return HttpResponseRedirect('/detail/' + checkcode + '/' + tid)
        # context = {'Response': 'Comment Success', 'url': '/detail/' + checkcode + '/' + tid}
        # return render(request, 'Res.html', context)
    except:
        context = {'Response': 'Please login', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)


def thumb(request, checkcode, tid, thid):
    try:
        user = User.objects.get(checkcode=checkcode)
        com = Com.objects.get(id=int(thid))
        com.thumb += 1
        com.save()
        return HttpResponseRedirect('/detail/' + checkcode + '/' + tid)
    except:
        context = {'Response': 'Please login', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)


def red1(request, tid):
    return HttpResponseRedirect('/login/register')


def red2(request, tid, thid):
    return HttpResponseRedirect('/login/register')
