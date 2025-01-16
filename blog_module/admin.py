from django.contrib import admin
from .models import *
from jalali_date.admin import ModelAdminJalaliMixin


class BlogAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'user', 'is_active', 'get_date_fa']
    list_editable = ['is_active']
    list_filter = ['date', 'is_active']


class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'is_published', 'get_date_fa']
    list_editable = ['is_published']
    list_filter = ['date', 'is_published']


admin.site.register(BlogModel, BlogAdmin)
admin.site.register(CommentModel, CommentAdmin)
