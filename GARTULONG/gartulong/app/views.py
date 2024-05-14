# views.py

from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'homepage.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')
