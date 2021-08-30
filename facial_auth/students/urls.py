
from django.urls import path 
from . import views
urlpatterns = [
    path('addstudent', views.addstudent, name='addstudent'),
    path('viewstudent', views.viewstudent, name='viewstudent'),
    path('webcam', views.webcam, name='webcam'),
    
     
 
]
