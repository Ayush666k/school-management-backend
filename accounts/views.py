from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from students.models import Student

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successfull')
                return redirect('login')
        else:
            messages.error(request, 'password do not match')
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfull!')
            return redirect('dashboards')
        else:
            messages.error(request, 'Invalid credentials')
            
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

