import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User, Info, Com, Mes
from login.views import refresh_code
from BBQ import settings
# Create your views here.


def clas(code, num):
    user = User.objects.get(checkcode=code)
    if user.clas >= num:
        return True
    else:
        return False


def admincheck(request, checkcode):
    try:
        user = User.objects.get(checkcode=checkcode)
        if user.clas == 3:
            u = User.objects.all()
            i = Info.objects.all()
            c = Com.objects.all()
            m = Mes.objects.all()
            context = {'ulist': u, 'ilist': i, 'clist': c, 'mlist': m, 'User': user}
            return render(request, 'admin/class3.html', context)
        elif user.clas == 2:
            i = Info.objects.all()
            c = Com.objects.all()
            context = {'ilist': i, 'clist': c, 'User': user}
            return render(request, 'admin/class2.html', context)
        else:
            return HttpResponseRedirect('/main/visitor/1')
    except:
        context = {'Response': 'Check failed', 'url': '/main/visitor/1'}
        return render(request, 'Res.html', context)


def show_edit(request, checkcode, tid):
    try:
        if clas(checkcode, 3):
            user = User.objects.get(id=int(tid))
            context = {'User': user, 'checkcode': checkcode, 'tid': str(user.id)}
            return render(request, 'admin/admin_edit.html', context)
    except:
        return HttpResponseRedirect('/main/visitor/1')


def delete(request, checkcode, item, tid):
    try:
        if item == 'user' and clas(checkcode, 3):
            user = User.objects.get(id=int(tid))
            mes = Mes.objects.filter(fromu=user.name)
            for m in mes:
                img_path = os.path.join(settings.IMG_UPLOAD_Mes, m.picture)
                try:
                    os.remove(img_path)
                except:
                    print('no picture')
            user.delete()
            mes.delete()
            #HttpResponseRedirect('/admin/' + checkcode)
            context = {'Response': 'Success', 'url': '/admin/' + checkcode}
            return render(request, 'Res.html', context)
        elif item == 'info' and clas(checkcode, 2):
            info = Info.objects.get(id=int(tid))
            img_path = os.path.join(settings.IMG_UPLOAD_Info, info.picture)
            try:
                os.remove(img_path)
            except:
                print('no picture')
            com = Com.objects.filter(tarInfo=int(tid))
            info.delete()
            com.delete()
            #HttpResponseRedirect('/admin/' + checkcode)
            context = {'Response': 'Success', 'url': '/admin/' + checkcode}
            return render(request, 'Res.html', context)
        elif item == 'com' and clas(checkcode, 2):
            com = Com.objects.get(id=int(tid))
            com.delete()
            #HttpResponseRedirect('/admin/' + checkcode)
            context = {'Response': 'Success', 'url': '/admin/' + checkcode}
            return render(request, 'Res.html', context)
        elif item == 'mes' and clas(checkcode, 3):
            mes = Mes.objects.get(id=int(tid))
            img_path = os.path.join(settings.IMG_UPLOAD_Mes, mes.picture)
            try:
                os.remove(img_path)
            except:
                print('no picture')
            mes.delete()
            #HttpResponseRedirect('/admin/' + checkcode)
            context = {'Response': 'Success', 'url': '/admin/' + checkcode}
            return render(request, 'Res.html', context)
        else:
            context = {'Response': 'Delete failed', 'url': '/admin/' + checkcode}
            return render(request, 'Res.html', context)
    except:
        return HttpResponseRedirect('/main/visitor/1')


def edit(request, checkcode, item, tid):
    try:
        if item == 'user' and clas(checkcode, 3):
            user = User.objects.get(id=int(tid))
            user.name = request.POST['name']
            user.password = request.POST['password']
            user.checkcode = refresh_code()
            user.clas = int(request.POST['class'])
            user.level = int(request.POST['level'])
            user.BBcoin = int(request.POST['BBcoin'])
            user.star = request.POST['star']
            user.save()
            context = {'Response': 'Success', 'url': '/admin/' + checkcode}
            return render(request, 'Res.html', context)
    except:
        return HttpResponseRedirect('/main/visitor/1')


