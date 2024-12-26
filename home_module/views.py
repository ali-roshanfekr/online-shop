from random import random

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from product_module.models import ProductModel
from site_setting_module.models import SliderModel, LogoModel


# Create your views here.

class HomeView(View):
    def get(self, request):
        # numbers = random.
        return render(request, 'index.html', {
            'products': ProductModel.objects.all()
        })

def header_component(request):
    logo = LogoModel.objects.filter(is_active=True).first()
    return render(request, 'header.html', {
        'logo': logo
    })

def footer_component(request):
    return render(request, 'footer.html', {

    })

def slider(request):
    return render(request, 'slider.html', {

    })

def sidebar(request):
    return render(request, 'sidebar.html', {

    })
