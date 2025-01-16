from django.contrib import admin

from .models import *


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'total', 'get_date_fa']
<<<<<<< HEAD
    list_filter = ['user', 'create_at']
=======
>>>>>>> 68f34a6 (complete shopping cart and set a number for each product.)


class InvoiceProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'number', 'get_date_fa']
<<<<<<< HEAD
    list_filter = ['product', 'number', 'create_at']
=======
>>>>>>> 68f34a6 (complete shopping cart and set a number for each product.)


admin.site.register(InvoiceModel, InvoiceAdmin)
admin.site.register(InvoiceProductModel, InvoiceProductAdmin)
