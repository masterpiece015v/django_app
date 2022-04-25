from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index( request ):
    if 'msg' in request.GET and 'myname' in request.GET:
        msg = request.GET['msg']
        result = 'you typed:{}'.format( msg )
    elif 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'you typed:{}'.format( msg )
    elif 'myname' in request.GET:
        myname = request.GET['myname']
        result = 'you typed:{}'.format( myname )
    else:
        result = 'please send msg parameter!'
    return HttpResponse( result )

def ok( request ):
    return HttpResponse("ok")
