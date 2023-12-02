from django.shortcuts import render
from main.models import User, Info
# Create your views here.


def m_page(request, checkcode, pid):
    try:
        user = User.objects.get(checkcode=checkcode)
        name = user.name
        url = '/user/' + checkcode
    except:
        name = 'visitor'
        url = '/login'
    info = []
    pid = int(pid)
    i = 1
    de = Info.objects.order_by('-id')
    upid = str(pid - 1)
    dpid = str(pid + 1)
    while i <= pid*10:
        try:
            if i > (pid-1)*10:
                info.append(de[i - 1])
            i += 1
        except:
            dpid = '0'
            break
    context = {'name': name, 'checkcode': checkcode, 'url': url,
               'info': info,
               'upid': upid, 'dpid': dpid}
    return render(request, 'main/main_page.html', context)


