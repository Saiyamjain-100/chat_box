from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('<str:Room>/',views.Room,name='Room'),
    path('checkroom',views.checkroom,name='checkroom'),
    path('send',views.send,name='send'),
    path('getMessages/<str:Room>/',views.getMessages,name='getMessages'),

]