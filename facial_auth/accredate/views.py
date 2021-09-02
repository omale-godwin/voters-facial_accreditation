import deepface
from django.http import request
from django.shortcuts import render, redirect
import sys
from django.contrib import messages, auth
import os
from django.http import JsonResponse
from PIL import Image
import numpy as np
from subprocess import PIPE, run
from deepface import DeepFace
from numpy.lib.type_check import imag
from .models import AdminAccreditation
from students.models import Student

# Create your views here.
def accredate(request):
    return render(request, 'accredate/accredate.html')

def adminlogin(request):
    # run([sys.executable, '//home//omale//Desktop//deepface/faces.py'], shell=False)
    return render(request, 'accredate/adminlogin.html')

def adminauth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            current_user = request.user
            print(current_user.username)
            messages.success(request, 'You are now logged in')
            return redirect('home')
    return render(request, 'accredate/adminlogin.html')

def student_auth(request):
      
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
    # DeepFace.stream(os.getcwd() + '/media/photos/', enable_face_analysis=False)
    run([sys.executable, os.getcwd() + '/fac.py'], shell=False) 
    
    # DeepFace.stream(os.getcwd(), enable_face_analysis=False, source='http://192.168.43.1:8080/video' )
    if os.path.isfile(os.getcwd() + '/my_image.png'):
        for i in  os.listdir(r'/home/omale/Music/facail_auth/facial_auth/media/photos'):
            print(os.getcwd() + '/media/photos/' + i)
            results = DeepFace.verify( os.getcwd() + '/my_image.png', os.getcwd() + '/media/photos/' + i, model_name = models[1], enforce_detection=False )
            if results['verified'] == True:
                request.session['users'] = i
                messages.success(request, 'welcome')
                return redirect('success_auth')
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            not_found = False
        messages.error(request, '𝕍𝕠𝕥𝕖𝕣 𝔽𝕒𝕔𝕚𝕒𝕝 𝔸𝕦𝕥𝕙𝕖𝕟𝕥𝕚𝕔𝕒𝕥𝕚𝕠𝕟 𝔽𝕒𝕚𝕝')
    else:
        messages.error('PLEASE RECAPTURE FACIAL IMAGE FOR ACCREDITATION')
        return redirect('accredate')
    context = {
        'not_found':not_found
    }
          
    # os.remove(os.getcwd() + '/my_image.png')
    return render(request, 'accredate/accredate.html', context)
def fail_auth(request):
    return render(request, 'accredate/fail_auth.html')
def conf(request):
    Auth_user = Student.objects.get(imag= 'photos/' + request.session['users'])
    Auth_user.confirm = True
    Auth_user.save()
    context = {
        'Auth_user':Auth_user
    }

    return render(request, 'accredate/success_auth.html', context)

def success_auth(request):
   
    Auth_user = Student.objects.get(imag= 'photos/' + request.session['users'])
    Auth_user.confirm = True
    
    context = {
        'Auth_user': Auth_user
    }
    return render(request, 'accredate/success_auth.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('adminauth')