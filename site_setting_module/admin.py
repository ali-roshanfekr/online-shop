from django.contrib import admin
from .models import *


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
    list_editable = ['is_active']


class LogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
    list_editable = ['is_active']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
    list_editable = ['is_active']


admin.site.register(SliderModel, SliderAdmin)
admin.site.register(LogoModel, LogoAdmin)
admin.site.register(LinkModel, LinkAdmin)
