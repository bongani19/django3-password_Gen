from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def aboutUs(request):
    return render(request,'generator/About.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))
    passwrd=""

    for x in range(length):
        passwrd += random.choice(characters)

    return render(request,'generator/password.html',{'password': passwrd})

#def con(request):
#    return render(request,'generator/About.html')
