import datetime
import os.path
from pathlib import Path

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User, Info, Mes
from BBQ import settings
# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent
pic = ['.jpg', '.tiff', '.png', '.gif', '.psd', '.raw', '.eps', '.svg', '.pdf', '.bmp']

def post_a(request, checkcode):
    context = {'checkcode': checkcode}
    return render(request, 'post/post_a.html', context)


def post_A(request, checkcode):
    try:
        user = User.objects.get(checkcode=checkcode)
        info = Info()
        try:
            li = Info.objects.last()
            iid = li.id + 1
        except:
            iid = 1
        try:
            img = request.FILES.get('img')
            # 获取图片的全文件名
            img_name = img.name
            if img.size <= 104857600:
                # 截取文件后缀和文件名
                mobile = str(iid)
                ext = os.path.splitext(img_name)[1]
                if ext in pic:
                    # 重定义文件名
                    img_name = f'avatar-{mobile}{ext}'
                    # 从配置文件中载入图片保存路径
                    img_path = os.path.join(settings.IMG_UPLOAD_Info, img_name)
                    # 写入文件
                    with open(img_path, 'ab') as fp:
                        # 如果上传的图片非常大，就通过chunks()方法分割成多个片段来上传
                        for chunk in img.chunks():
                            fp.write(chunk)
                else:
                    context = {'Response': '非图片类型', 'url': '/user/' + checkcode}
                    return render(request, 'Res.html', context)
            else:
                context = {'Response': '图片过大', 'url': '/user/' + checkcode}
                return render(request, 'Res.html', context)
        except:
            img_name = ''
        info.id = iid
        info.sid = str(iid)
        info.title = request.POST['title']
        info.text = request.POST['text']
        info.picture = img_name
        info.gift = '0/0/0/0'
        info.fromu = user.name
        info.hide = request.POST['hide']
        info.pub_time = datetime.datetime.now()
        info.save()
        return HttpResponseRedirect('/detail/' + checkcode + '/' + str(iid))
        # context = {'Response': 'Post Success', 'url': '/user/' + checkcode}
        # return render(request, 'Res.html', context)
    except:
        context = {'Response': '发布失败', 'url': '/user/' + checkcode}
        return render(request, 'Res.html', context)


def post_M(request, checkcode):
    try:
        tarn = str(request.POST['tar'])
        fromu = User.objects.get(checkcode=checkcode)
        taru = User.objects.get(name=tarn)
        mes = Mes()
        try:
            li = Mes.objects.last()
            iid = li.id + 1
        except:
            iid = 1
        try:
            img = request.FILES.get('img')
            # 获取图片的全文件名
            img_name = img.name
            if img.size <= 104857600:
                # 截取文件后缀和文件名
                mobile = str(iid)
                ext = os.path.splitext(img_name)[1]
                if ext in pic:
                    # 重定义文件名
                    img_name = f'avatar-{mobile}{ext}'
                    # 从配置文件中载入图片保存路径
                    img_path = os.path.join(settings.IMG_UPLOAD_Mes, img_name)
                    # 写入文件
                    with open(img_path, 'ab') as fp:
                        # 如果上传的图片非常大，就通过chunks()方法分割成多个片段来上传
                        for chunk in img.chunks():
                            fp.write(chunk)
                else:
                    context = {'Response': '非图片类型', 'url': '/user/' + checkcode}
                    return render(request, 'Res.html', context)
            else:
                context = {'Response': '图片过大', 'url': '/user/' + checkcode}
                return render(request, 'Res.html', context)
        except:
            img_name = ''

        mes.id = iid
        mes.fromu = fromu.name
        mes.taru = taru.name
        mes.text = request.POST['text']
        mes.picture = img_name
        mes.time = datetime.datetime.now()
        mes.save()
        return HttpResponseRedirect('/user/' + checkcode)
        # context = {'Response': 'Post Success', 'url': '/user/' + checkcode}
        # return render(request, 'Res.html', context)
    except:
        context = {'Response': '发送失败', 'url': '/user/' + checkcode}
        return render(request, 'Res.html', context)
