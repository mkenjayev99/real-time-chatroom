from rest_framework import generics
from .models import Message
from django.shortcuts import render, redirect
from .models import Room
from .serializers import RoomSerializer


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat.html", context)


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    ctx = {
        'room_name': room_name,
        'username': username,
        'messages': messages
    }
    return render(request, 'room.html', ctx)

