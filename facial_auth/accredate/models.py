from django.db import models

# Create your models here.
class AdminAccreditation(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    names = models.CharField(max_length=200)
    faceAdmin = models.ImageField()
    def __str__(self):
        return self.username