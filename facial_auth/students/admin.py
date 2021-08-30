from django.contrib import admin
from .models import Student
# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'reg_number', 'phone', 'emailA', 'department', 'imag', 'confirm')
    list_display_links = ('id', 'fullname', 'reg_number' )
    list_filter = ('fullname', 'reg_number', 'phone')
    list_per_page = 25
    

admin.site.register(Student, AdminStudent)
    