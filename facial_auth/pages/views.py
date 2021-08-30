from os import pipe
from django.shortcuts import render, redirect
from deepface import DeepFace
from django.contrib import messages
import os
from subprocess import run, PIPE
import sys
from accredate.models import AdminAccreditation

# Create your views here.
def Home(request):
    admindata = AdminAccreditation.objects.get(id=1)
    context = {
        'admindata': admindata
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')