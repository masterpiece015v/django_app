from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
# Create your views here.

def index( request ):
    p = {
        'title':'Hello/Index',
        'msg':'これは、サンプルで作ったページです',
        'goto':'next',
        'page1':'page1',
        'form':HelloForm(),
    }
    if(request.method=='POST'):
        p['msg'] = "名前:{}<br>メール:{}<br>年齢:{}".format(
            request.POST['name'],
            request.POST['mail'],
            request.POST['age'])
    return render(request,'hello/index.html',p)

def ok( request ):
    return HttpResponse("ok")

def next(request):
    p = {
        'title':'Hello/Next',
        'msg' : 'これは、もう一つのページです。',
        'goto' : 'index',
        'page1':'page1',
    }
    return render( request, 'hello/index.html', p )

def page1(request):
    p = {
        'title':'Hello/Next',
        'msg' : 'これは、もう一つのページです。',
        'goto' : 'index',
        'page1':'next',
    }
    return render( request , 'hello/index.html',p)

def form( request ):
    msg = request.POST['msg']
    age = request.POST['age']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは{}さん。年齢は{}です。'.format(msg,age),
        'goto':'index',
        'page1':'next'
    }
    return render( request , 'hello/index.html' , params )
