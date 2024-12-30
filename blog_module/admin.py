from django.contrib import admin
from .models import BlogModel
from jalali_date.admin import ModelAdminJalaliMixin


class BlogAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'user', 'is_active', 'get_date_fa']
    list_editable = ['is_active']
    list_filter = ['date', 'is_active']


admin.site.register(BlogModel, BlogAdmin)
