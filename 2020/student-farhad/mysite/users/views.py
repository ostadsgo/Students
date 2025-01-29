from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']
        u = User(username=email, email=email, password=psw)
        u.save()
        return redirect('user_login')

    else:
        return render(request, 'users/register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']
        
        x = User.objects.get(username=email)
        if x.password == psw:
            login(request, x)
            return redirect('home')

    return render(request, 'users/login.html')