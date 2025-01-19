import logging
import random

from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from product_module.models import ProductModel, CategoryModel
from site_setting_module.models import *

text = None
category = None


class HomeView(View):
    def get(self, request):
        try:
            if text is None and category is None:
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

            else:
                if category != 'All':
                    products = ProductModel.objects.filter(title__contains=str(text), category__slug=category)

                else:
                    products = ProductModel.objects.filter(title__contains=str(text))

                paginator = Paginator(products, 6)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                print(page_obj)
                for p in products:
                    print(p.title)
                return render(request, 'index.html', {
                    'page_obj': page_obj,
                    'paginator': paginator,
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')

    def post(self, request):
        try:
            global text, category

            text = request.POST.get('text')
            category = request.POST.get('category')
            if category != 'All':
                products = ProductModel.objects.filter(title__contains=str(text), category__slug=category)

            else:
                products = ProductModel.objects.filter(title__contains=str(text))

            paginator = Paginator(products, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            print(page_obj)
            for p in products:
                print(p.title)
            return render(request, 'index.html', {
                'page_obj': page_obj,
                'paginator': paginator,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')


def header_component(request):
    try:
        logo = LogoModel.objects.filter(is_active=True).first()
        categories = CategoryModel.objects.all()
        return render(request, 'header.html', {
            'logo': logo,
            'categories': categories
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')
        return redirect('error')


def footer_component(request):
    try:
        links = LinkModel.objects.filter(is_active=True)
        return render(request, 'footer.html', {
            'links': links,
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')
        return redirect('error')


def slider(request):
    try:
        slides = SliderModel.objects.filter(is_active=True)
        return render(request, 'slider.html', {
            'slides': slides
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')
        return redirect('error')


def sidebar(request):
    try:
        categories = CategoryModel.objects.all()
        random_product_1 = random.choice(ProductModel.objects.all())
        random_product_2 = random.choice(ProductModel.objects.all())
        return render(request, 'sidebar.html', {
            'categories': categories,
            'random_product_1': random_product_1,
            'random_product_2': random_product_2
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')
        return redirect('error')


def scripts(request):
    try:
        return render(request, 'scripts.html', {

        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')
        return redirect('error')


class UserExit(View):
    def post(self, request):
        global text, category
        text = None
        category = None

        return JsonResponse({'status': 'success'})



class ErrorView(View):
    def get(self, request):
        raise Http404
