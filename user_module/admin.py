from django.contrib import admin
from .models import *
from jalali_date.admin import ModelAdminJalaliMixin


class UserAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['username', 'get_date_fa']
    list_filter = ['is_staff', 'is_active', 'last_login']


admin.site.register(User, UserAdmin)
