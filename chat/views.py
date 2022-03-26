from django.shortcuts import render
from matplotlib.style import context

# Create your views here.


def home(request):
    return render(request, "chat/home.html")


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    context = {"room_name": room_name}
    return render(request, "chat/room.html", context)
