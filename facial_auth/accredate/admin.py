from django.contrib import admin
from .models import AdminAccreditation
# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'names','faceAdmin')
    list_display_links = ('id', 'username', 'names')
    list_filter = ('username',)
    list_per_page = 20

admin.site.register(AdminAccreditation, AdminUser)