from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'account/login.html')

def view_login(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        user = authenticate(username=login_username, password=login_password)
        if user is not None:
            login(request, user)
    return redirect('/')

def view_logout(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
    return redirect('/')

def signup(request):
    return render(request, 'account/signup.html')

def new_account(request):
    if request.method == 'POST':
        new_username = request.POST['new_username']
        new_email = request.POST['new_email']
        new_password = request.POST['new_password']
        user = User.objects.create_user(new_username, new_email, new_password)
        user = authenticate(username=new_username, password=new_password)
        login(user)
    return redirect('/')