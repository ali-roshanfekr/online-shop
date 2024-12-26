from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_login']
    list_filter = ['is_staff', 'is_active']


admin.site.register(User, UserAdmin)
