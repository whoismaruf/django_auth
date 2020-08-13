from django.shortcuts import render


def index(request):
    return render(request, 'root/index.html')


def register_view(request):
    return render(request, 'auth/register.html')


def login_view(request):
    return render(request, 'auth/login.html')


def forgot(request):
    return render(request, 'auth/forgot.html')