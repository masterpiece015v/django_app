from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ok' , views.ok , name='ok'),
    path('next',views.next,name='next'),
    path('page1',views.page1,name='page1'),
    path('form',views.form,name='form'),
]
