from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'number']
    list_filter = ['price', 'number']
    list_editable = ['price', 'is_active', 'number']
    prepopulated_fields = {
        'slug': ['title']
    }


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(BrandModel, BrandAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
