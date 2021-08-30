
import os
import shutil
from django.http import request
from django.shortcuts import redirect, render
from datetime import datetime
from django.conf import settings 
from numpy.lib.type_check import imag
from .models import Student
from django.http import HttpResponse
from subprocess import PIPE, run
import sys
from django.core.files import File




# Create your views here.
def addstudent(request):
    if request.method == 'POST':      
        fullname = request.POST['firstname']
        reg_number = request.POST['reg_number']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        emailA = request.POST['emailA']
        description = request.POST['description']
        department= request.POST['department']
        gender = request.POST['gender']
        states = request.POST['states']
        contry = request.POST['contry']
        local_government = request.POST['local_government']
        myfile = 'photos/' + fullname + '.png'
        postcode = request.POST['postcode'] 
        namin = fullname + '.png'
        os.rename('my_image.png', namin)
        src_dir = os.getcwd() + '/' + namin
        dst_dir = os.getcwd() + '/media/photos'
        shutil.copy(src_dir, dst_dir )
        os.remove(src_dir)
        
        
     

        save_data = Student(fullname=fullname, imag=myfile,  reg_number=reg_number, phone=phone, address=address, dob=dob, emailA=emailA, description=description, department=department, gender=gender, states=states, contry=contry, local_government=local_government, postcode=postcode)
        save_data.save()


  
        

    return render(request, 'student/addstudent.html')

def viewstudent(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('ereffffffffffffffffffffff')
    print(os.getcwd() + '/media/photos')
    
    print('gggggggggggggggggg')
   
    print(os.getcwd())
    student_all = Student.objects.all()
    context = {
        'students': student_all
    }
    return render(request, 'student/viewstudent.html', context)

def webcam(request):
    run([sys.executable, '//home//omale//Desktop//deepface/faces.py'], shell=False)
    print('omaleeeeeeeeeeeeeeeeeeeeee')
    return redirect('addstudent')