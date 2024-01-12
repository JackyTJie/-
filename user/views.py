from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import User, Info, Com
from login.views import refresh_code
# Create your views here.


def u_page(request, checkcode):
    try:
        user = User.objects.get(checkcode=checkcode)
        info = Info.objects.filter(fromu=user.name)
        com = Com.objects.filter(fromu=user.name)
        tar_det = str(user.star).split('/')
        tar_info = []
        for tid in tar_det:
            try:
                tar_info.append(Info.objects.get(id=int(tid)))
            except:
                print('not get')
        context = {'User': user, 'info': info, 'com': com, 'star': tar_info}
        return render(request, 'user/user_page.html', context)
    except:
        context = {'Response': 'Please login', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)


def v_page(request, checkcode, uname):
    try:
        user_v = User.objects.get(checkcode=checkcode)
        user_h = User.objects.get(name=uname)
        info = Info.objects.filter(fromu=uname)
        s_info = []
        for i in info:
            if i.hide == 'False':
                s_info.append(i)
        context = {'checkcode': checkcode, 'uname': uname, 'ulevel': str(user_h.level), 'info': s_info}
        return render(request, 'user/visit_page.html', context)
    except:
        context = {'Response': 'Please login', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)


def log(request):
    return HttpResponseRedirect('/login/register')


def log2(request, uname):
    return HttpResponseRedirect('/login/register')


def game_1(request):
    return HttpResponseRedirect('/static/system/Small games/Game 1/index.html')


def show_reset(request, checkcode):
    try:
        user = User.objects.get(checkcode=checkcode)
        context = {'checkcode': checkcode, 'User': user}
        return render(request, 'login/reset.html', context)
    except:
        context = {'Response': 'Please login', 'url': '/login'}
        return render(request, 'Res.html', context)


def reset(request, checkcode):
    try:
        user = User.objects.get(checkcode=checkcode)
        user.password = request.POST['password']
        newcheck = refresh_code()
        user.checkcode = newcheck
        user.save()
        return HttpResponseRedirect('/user/' + newcheck)
    except:
        context = {'Response': 'Please login', 'url': '/login'}
        return render(request, 'Res.html', context)
