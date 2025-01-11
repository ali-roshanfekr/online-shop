from django.contrib import admin

from .models import *


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'total', 'get_date_fa']


class InvoiceProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'number', 'get_date_fa']


admin.site.register(InvoiceModel, InvoiceAdmin)
admin.site.register(InvoiceProductModel, InvoiceProductAdmin)
