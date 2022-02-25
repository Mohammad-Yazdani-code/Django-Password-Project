import re
from tokenize import Special
from django.shortcuts import render
from django.http import HttpResponse
import random

from numpy import character
# Create your views here.

def home(request):
    return render(request, 'generator/index.html')
#______________________________________________________________________________
def Password(request):
    Character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('Uppercase'):
        Character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        Character.extend(list('0123456789'))
    if request.GET.get('special'):
        Character.extend(list('!@#$%^&'))   
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(Character)
    return render(request, 'generator/Password.html', {"Password":thepassword})
#_____________________________________________________________________________________
def about(request):
    return render(request, 'generator/aboutus.html')