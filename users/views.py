
from django.shortcuts import redirect, render
from matplotlib.style import context
from django.contrib.auth import authenticate, login
from users import form
from users.form import CreateRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import Group


# Create your views here.


def register(request):
    form = CreateRegisterForm()
    if request.method == "POST":
        form = CreateRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='clients')
            user.groups.add(group)
            messages.success(request, "Account created successful "+username)
            return redirect('login')
    context = {'form': form}
    return render(request, "users/register.html", context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, ' Username or Password is incorrect')
    context = {}
    return render(request, "users/login.html", context)
