
from django.urls import path 
from . import views
urlpatterns = [   
    path('accredate', views.accredate, name='accredate'),
    path('adminauth', views.adminauth, name='adminauth'),
    path('', views.adminlogin, name='adminlogin'),
    path('student_auth', views.student_auth, name='student_auth'),
    path('success_auth', views.success_auth, name='success_auth'),
    path('fail_auth', views.fail_auth, name='fail_auth'),
    path('logout', views.logout, name='logout'),
    path('conf', views.conf, name='conf'),
    
    
]
