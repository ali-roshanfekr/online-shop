import random
from django.shortcuts import render
from django.views import View
from product_module.models import ProductModel
from site_setting_module.models import *


class HomeView(View):
    def get(self, request):
        products = ProductModel.objects.all().order_by('price')
        featured_products = []
        latest_products = products[0:6]

        for i in range(4):
            product = random.choice(products)
            featured_products.append(product)

        return render(request, 'index.html', {
            'featured_products': featured_products,
            'latest_products': latest_products
        })


def header_component(request):
    logo = LogoModel.objects.filter(is_active=True).first()
    return render(request, 'header.html', {
        'logo': logo
    })


def footer_component(request):
    ins_link = LinkModel.objects.filter(title='instagram', is_active=True).first()
    return render(request, 'footer.html', {
        'ins_link': ins_link,
    })


def slider(request):
    return render(request, 'slider.html', {

    })


def sidebar(request):
    return render(request, 'sidebar.html', {

    })
