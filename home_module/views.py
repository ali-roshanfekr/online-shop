import logging
import random

from django.http import Http404
from django.shortcuts import render
from django.views import View

from product_module.models import ProductModel
from site_setting_module.models import *


class HomeView(View):
    def get(self, request):
        try:
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

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error('This is an error message.', e)


def header_component(request):
    try:
        logo = LogoModel.objects.filter(is_active=True).first()
        return render(request, 'header.html', {
            'logo': logo
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)


def footer_component(request):
    try:
        ins_link = LinkModel.objects.filter(title='instagram', is_active=True).first()
        return render(request, 'footer.html', {
            'ins_link': ins_link,
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)


def slider(request):
    try:
        return render(request, 'slider.html', {

        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)


def sidebar(request):
    try:
        return render(request, 'sidebar.html', {

        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
