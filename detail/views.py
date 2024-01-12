from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import User, Info, Com
# Create your views here.


def detail(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
    except:
        user = 'visitor'
    info = Info.objects.get(id=int(tid))
    com = Com.objects.filter(tarInfo=int(tid))
    time = info.pub_time.split('.')[0]
    st = info.gift.split('/')[0]
    nd = info.gift.split('/')[1]
    rd = info.gift.split('/')[2]
    th = info.gift.split('/')[3]
    if info.hide == 'True':
        aut = 'revealed'
    else:
        aut = info.fromu
    context = {'author': aut, 'title': info.title, 'text': info.text, 'img': info.picture, 'st': st, 'nd': nd, 'rd': rd,
               'th': th, 'com': com, 'tid': tid, 'time': time, 'user': user}
    return render(request, 'detail/detail_page.html', context)


def star(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
        slist = user.star.split('/')
        stared = False
        for s in slist:
            if str(tid) == str(s):
                stared = True
        if not stared:
            user.star = user.star + '/' + tid
            user.save()
        return HttpResponseRedirect('/detail/' + checkcode + '/' + tid)
    except:
        context = {'Response': 'Please login', 'url': '/login'}
        return render(request, 'Res.html', context)


def unstar(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
        user.star = str(user.star).replace('/'+tid, '')
        user.save()
        return HttpResponseRedirect('/user/' + checkcode)
    except:
        context = {'Response': 'Please login', 'url': '/login'}
        return render(request, 'Res.html', context)


def show_gift(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
        context = {'User': user, 'id': tid}
        return render(request, 'detail/gift.html', context)
    except:
        context = {'Response': 'Please login', 'url': '/login'}
        return render(request, 'Res.html', context)


def gift(request, checkcode, tid):
    try:
        user = User.objects.get(checkcode=checkcode)
        info = Info.objects.get(id=int(tid))
        o = request.POST['type']
        num = int(request.POST['num'])
        st = int(info.gift.split('/')[0])
        nd = int(info.gift.split('/')[1])
        rd = int(info.gift.split('/')[2])
        th = int(info.gift.split('/')[3])
        if o == '1st':
            cost = num * 10
            gif = num * 8
            if user.BBcoin > cost:
                st += num
        elif o == '2nd':
            cost = num * 66
            gif = num * 55
            if user.BBcoin > cost:
                nd += num
        elif o == '3rd':
            cost = num * 88
            gif = num * 77
            if user.BBcoin > cost:
                rd += num
        elif o == '4th':
            cost = num * 100
            gif = num * 90
            if user.BBcoin > cost:
                th += num
        if user.BBcoin > cost:
            user.BBcoin -= cost
            user.save()
            rec = User.objects.get(name=info.fromu)
            rec.BBcoin += gif
            rec.save()
        else:
            context = {'Response': 'BBcoin不够哟', 'url': '/user/' + user.checkcode}
            return render(request, 'Res.html', context)
        info.gift = str(st) + '/' + str(nd) + '/' + str(rd) + '/' + str(th)
        info.save()
        return HttpResponseRedirect('/detail/' + user.checkcode + '/' + tid)
    except:
        context = {'Response': 'Please login', 'url': '/login'}
        return render(request, 'Res.html', context)



def red(request, tid):
    return HttpResponseRedirect('/login/register')
