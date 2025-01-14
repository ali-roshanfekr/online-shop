from django.contrib import admin
from .models import *
from jalali_date.admin import ModelAdminJalaliMixin


class UserAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['username', 'get_date_fa']
    list_filter = ['is_staff', 'is_active', 'last_login']


class CityAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title']


class StateAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title']


admin.site.register(User, UserAdmin)
admin.site.register(CityModel, CityAdmin)
admin.site.register(StateModel, StateAdmin)
