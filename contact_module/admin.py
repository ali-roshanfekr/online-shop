from django.contrib import admin
from .models import *
from jalali_date.admin import ModelAdminJalaliMixin


class ContactAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['email', 'get_date_fa', 'title']


admin.site.register(ContactModel, ContactAdmin)
