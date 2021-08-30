from django.db import models
from django.db.models.fields.files import ImageFileDescriptor
from datetime import datetime
# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=200, null=True, blank=True)
    reg_number = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    emailA = models.EmailField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    states = models.CharField(max_length=200, null=True, blank=True)
    contry = models.CharField(max_length=200, null=True, blank=True)
    local_government = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True, blank=True)
    imag = models.ImageField(upload_to='photos', null=True, blank=True)
    confirm = models.BooleanField(default=False)
    def __str__(self):
        return self.fullname