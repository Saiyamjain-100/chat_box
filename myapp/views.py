from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from myapp.models import room, message

# Create your views here.
def index(request):
    return render(request,'index.html')

def Room(request,Room):
    username= request.GET.get('username')
    room_details= room.objects.get(name=Room)
    return render(request,'Room.html',{'username':username,'Room':Room,'room_details':room_details})


def checkroom(request):
    Room =request.POST['room_name']
    username =request.POST['user_name']

    if room.objects.filter(name=Room).exists():
        return redirect('/'+Room+'/?username='+username)
    else:
        new_room=room.objects.create(name=Room)
        new_room.save()
        return redirect('/'+Room+'/?username='+username)

def send(request):
    Message = request.POST['Message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = message.objects.create(value=Message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message set successfully')

def getMessages(request,Room):
    room_details = room.objects.get(name=Room)

    messages=message.objects.filter(Room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})