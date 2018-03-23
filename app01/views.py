from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection


def index(request):
    """进入首页"""

    #连接到redis数据库，返回一个Strictredis对象
    #default表示上面setting文件中CACHES中的配置
    strict_redis = get_redis_connection('default')

    #保存一个string类型的键值对
    strict_redis.hset('uname','name','hahahax')
    strict_redis.hset('uname','vcode','123')

    #获取string类型的值
    name = strict_redis.hget('uname','name')
    vcode = strict_redis.hget('uname','vcode')

    text = 'name = %s <br/>vcode = %s' % (name,vcode)

    return HttpResponse(text)


def set_session(request):
    request.session['name'] = 'python01'
    request.session['vcode'] = '1234'
    # strict_redis = get_redis_connection('default')
    #
    # #保存一个string类型的键值对
    # strict_redis.hset('session','name','hahahax')
    # strict_redis.hset('session','vcode','12345')
    return HttpResponse('保存成功')


def get_session(request):
    name = request.session.get('name')
    vcode = request.session.get('vcode')
    text = 'name = %s <br/>vcode = %s' % (name,vcode)
    return HttpResponse(text)


def show_goods(request):

    return render(request,'show_goods.html')