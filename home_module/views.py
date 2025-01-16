import logging
import random

from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from product_module.models import *
from site_setting_module.models import *
from site_setting_module.models import SliderModel

val = None
category = None


class HomeView(View):
    def get(self, request):
        try:
            if val or category:
                if category == 'All':
                    products = ProductModel.objects.filter(title__contains=str(val))

                else:
                    products = ProductModel.objects.filter(title__contains=str(val), category__slug=str(category))

                paginator = Paginator(products, 6)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)

                return render(request, 'index.html', {
                    'page_obj': page_obj,
                    'paginator': paginator,
                    'permission': True
                })

            else:
                products = ProductModel.objects.all().order_by('price')
                featured_products = []
                latest_products = products[0:6]

                for i in range(4):
                    product = random.choice(products)
                    featured_products.append(product)

                return render(request, 'index.html', {
                    'featured_products': featured_products,
                    'latest_products': latest_products,
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error('This is an error message.', e)
            return redirect('arandomaddress')

    def post(self, request):
        try:
            if request.POST.get('search-button') == 'search':
                global val, category

                val = request.POST.get('search-box')
                category = request.POST.get('select-box')
                if category == 'All':
                    products = ProductModel.objects.filter(title__contains=str(val))

                else:
                    products = ProductModel.objects.filter(title__contains=str(val), category__slug=str(category))

                paginator = Paginator(products, 6)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)

                return render(request, 'index.html', {
                    'page_obj': page_obj,
                    'paginator': paginator,
                    'permission': True
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error('This is an error message.', e)
            return redirect('arandomaddress')


def header_component(request):
    if request.method == 'GET':
        try:
            logo = LogoModel.objects.filter(is_active=True).first()
            categories = CategoryModel.objects.all()
            return render(request, 'header.html', {
                'logo': logo,
                'categories': categories
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error('This is an error message.', e)
            return redirect('arandomaddress')

    if request.method == 'POST':
        try:
            logo = LogoModel.objects.filter(is_active=True).first()
            categories = CategoryModel.objects.all()
            return render(request, 'header.html', {
                'logo': logo,
                'categories': categories
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error('This is an error message.', e)
            return redirect('arandomaddress')


def footer_component(request):
    try:
        ins_link = LinkModel.objects.filter(title='instagram', is_active=True).first()
        return render(request, 'footer.html', {
            'ins_link': ins_link,
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
        return redirect('arandomaddress')


def slider(request):
    try:
        slides = SliderModel.objects.filter(is_active=True)
        return render(request, 'slider.html', {
            'slides': slides,
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
        return redirect('arandomaddress')


def sidebar(request):
    try:
        categories = CategoryModel.objects.all()
        products = ProductModel.objects.all()
        return render(request, 'sidebar.html', {
            'categories': categories,
            'product_1': random.choice(products),
            'product_2': random.choice(products)
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
        return redirect('arandomaddress')


def scripts(request):
    try:
        return render(request, 'scripts.html', {

        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
        return redirect('arandomaddress')


class UserExit(View):
    def get(self, request):
        pass

    def post(self, request):
        global val, category

        val = None
        category = None

        return JsonResponse({'status': 'success'})

