from django.shortcuts import render
import random


# Create your views here.

def home(request):
    return render(request, 'home.html')

def password(request):
    password = ""
    charaters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        charaters.extend(list('1234567890'))

    if request.GET.get('special'):
        charaters.extend(list('~!@#$%^&*()_+{}":"'))
    for char in range(length):
        password = password + random.choice(charaters)

    return render(request, 'password.html', {'password':password})

def about(request):
    return render(request, 'about.html')
