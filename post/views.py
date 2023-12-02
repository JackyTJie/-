import os.path
from pathlib import Path

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User, Info
from BBQ import settings
# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent


def post_a(request, checkcode):
    context = {'checkcode': checkcode}
    return render(request, 'post/post_a.html', context)


def post_A(request, checkcode):
    try:
        user = User.objects.get(checkcode=checkcode)
        info = Info()
        try:
            img = request.FILES.get('img')
            # 获取图片的全文件名
            img_name = img.name
            # 截取文件后缀和文件名
            mobile = os.path.splitext(img_name)[0]
            ext = os.path.splitext(img_name)[1]
            # 重定义文件名
            img_name = f'avatar-{mobile}{ext}'
            # 从配置文件中载入图片保存路径
            img_path = os.path.join(settings.IMG_UPLOAD, img_name)
            # 写入文件
            with open(img_path, 'ab') as fp:
                # 如果上传的图片非常大，就通过chunks()方法分割成多个片段来上传
                for chunk in img.chunks():
                    fp.write(chunk)
            print('pass')
        except:
            img_name = ''
        try:
            li = Info.objects.last()
            iid = li.id + 1
        except:
            iid = 1
        info.id = iid
        info.sid = str(iid)
        info.title = request.POST['title']
        info.text = request.POST['text']
        info.picture = img_name
        info.gift = 'None'
        info.fromu = user.name
        info.hide = request.POST['hide']
        info.save()
        return HttpResponseRedirect('/detail/' + checkcode + '/' + str(iid))
        # context = {'Response': 'Post Success', 'url': '/user/' + checkcode}
        # return render(request, 'Res.html', context)
    except:
        context = {'Response': 'Post failed', 'url': '/user/' + checkcode}
        return render(request, 'Res.html', context)
