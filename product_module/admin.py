from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active']
    list_filter = ['price']
    list_editable = ['price', 'is_active']
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
