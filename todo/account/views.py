from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'account/login.html')

def login(request):
    pass

def signup(request):
    return render(request, 'account/signup.html')

def new_account(request):
    return render(request, 'account/signup.html')