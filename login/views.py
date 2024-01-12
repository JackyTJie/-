import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User
# Create your views here.

character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             '1','2','3','4','5','6','7','8','9','0']

def refresh_code():
    finish = -1
    while finish < 0:
        finish = 1
        code = ''
        for t in range(10):
            code += character[random.randrange(62)]
        for user in User.objects.all():
            if code == user.checkcode:
                finish = -1
    return code


def login(request):
    return render(request, 'login/login_page.html')


def checkupdate(request):
    try:
        user = User.objects.get(name=request.POST['name'])
        if str(user.password) == str(request.POST['password']):
            code = refresh_code()
            user.checkcode = code
            user.save()
            return HttpResponseRedirect('/main/' + code + '/1')
            # context = {'Response': 'Success', 'url': '/user/' + code}
        else:
            context = {'Response': '密码错误', 'url': '/login'}
    except:
        context = {'Response': '用户不存在', 'url': '/login/register'}
    return render(request, 'Res.html', context)


def register(request):
    return render(request, 'login/register_page.html')


def reg_op(request):
    try:
        User.objects.get(name=request.POST['name'])
        context = {'Response': '用户名已被占用', 'url': '/login/register'}
        return render(request, 'Res.html', context)
        # context = {'Response': 'Success', 'url': '/main/' + code + '/1'}
        # return render(request, 'Res.html', context)
    except:
        if request.POST['check'] == 'con':
            user = User()
            try:
                ul = User.objects.last()
                nid = ul.id + 1
            except:
                nid = 1
            user.id = nid
            user.name = request.POST['name']
            code = refresh_code()
            user.checkcode = code
            user.password = request.POST['password']
            user.clas = 0
            user.level = 1
            user.BBcoin = 0
            user.star = '1'
            user.save()
            return HttpResponseRedirect('/main/' + code + '/1')
        else:
            context = {'Response': '请同意用户协议', 'url': '/login/register'}
            return render(request, 'Res.html', context)


def con(request):
    return render(request, 'login/user_contract.html')




