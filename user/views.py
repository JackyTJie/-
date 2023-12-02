from django.shortcuts import render
from main.models import User, Info, Com
# Create your views here.


def u_page(request, checkcode):
    user = User.objects.get(checkcode=checkcode)
    info = Info.objects.filter(fromu=user.name)
    com = Com.objects.filter(fromu=user.name)
    context = {'User': user, 'info': info, 'com': com}
    return render(request, 'user/user_page.html', context)


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
