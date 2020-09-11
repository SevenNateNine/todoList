from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'account/login.html')

def login(request):
    pass

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