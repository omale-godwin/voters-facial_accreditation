import deepface
from django.http import request
from django.shortcuts import render, redirect
import sys
from django.contrib import messages
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
    run([sys.executable, '//home//omale//Desktop//deepface/faces.py'], shell=False)   
    results = DeepFace.verify( os.getcwd() + '/my_image.png', os.getcwd() + '/media/my_image.png', enforce_detection=False)
    os.remove(os.getcwd() + '/my_image.png')
    print(results)
    if results['verified'] == False:
        messages.error(request, 'Facial Authentication Fail!!!')
        return redirect('/') 
    if results['verified'] == True:
        return redirect('home')
    return render(request, 'accredate/adminauth.html')

def student_auth(request):
      
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
    # DeepFace.stream(os.getcwd() + '/media/photos/', enable_face_analysis=False)
    run([sys.executable, '//home//omale//Desktop//deepface/faces.py'], shell=False) 
    
    # DeepFace.stream(os.getcwd(), enable_face_analysis=False, source='http://192.168.43.1:8080/video' )
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
    context = {
        'not_found':not_found
    }
          
    # os.remove(os.getcwd() + '/my_image.png')
    return render(request, 'accredate/accredate.html', context)
def fail_auth(request):
    return render(request, 'accredate/fail_auth.html')

def success_auth(request):
    if request.method == 'POST':
        Auth_user = Student.objects.get(imag= 'photos/' + request.session['users'])
        Auth_user.confirm = True
   
    Auth_user = Student.objects.get(imag= 'photos/' + request.session['users'])
    context = {
        'Auth_user': Auth_user
    }
    return render(request, 'accredate/success_auth.html', context)

