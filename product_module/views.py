import logging

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views import View

from .models import *

brand_title = None


class ProductView(View):
    def get(self, request, slug):
        try:
            category = CategoryModel.objects.filter(slug=slug).first()
            if brand_title is not None:
                brand = BrandModel.objects.filter(title=brand_title).first()
                products = ProductModel.objects.filter(category=category, brand=brand)
            else:
                products = ProductModel.objects.filter(category=category)

            paginator = Paginator(products, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            brands = BrandModel.objects.all()
            return render(request, 'products.html', context={
                'page_obj': page_obj,
                'paginator': paginator,
                'brands': brands,
                'slug': slug,
                'permission': True
            })

        except Exception as e:
            logging.error('An error occurred: ', e)
            raise Http404

    def post(self, request, slug):
        try:
            global brand_title

            category = CategoryModel.objects.filter(slug=slug).first()
            brand_title = request.POST['brand']
            brand = BrandModel.objects.filter(title=brand_title).first()
            if brand is not None:
                products = ProductModel.objects.filter(category=category, brand=brand)
            else:
                products = ProductModel.objects.filter(category=category)
            paginator = Paginator(products, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            brands = BrandModel.objects.all()
            return render(request, 'products.html', context={
                'page_obj': page_obj,
                'paginator': paginator,
                'brands': brands,
                'slug': slug,
                'permission': True
            })

        except Exception as e:
            logging.error('An error occurred: ', e)
            raise Http404


class CategoryView(View):
    def get(self, request):
        try:
            categories = CategoryModel.objects.all()
            return render(request, 'category.html', {
                'categories': categories
            })

        except Exception as e:
            logging.error('An error occurred: ', e)
            raise Http404


class ProductDetailsView(View):
    def get(self, request, slug):
        try:
            product = ProductModel.objects.filter(slug=slug).first()
            brands = ''
            number = 0
            for brand in product.brand.all():
                if number == 0:
                    brands += brand.title
                    number = 1

                else:
                    brands += ', ' + brand.title

            return render(request, 'product_details.html', {
                'product': product,
                'brands': brands
            })

        except Exception as e:
            logging.error('An error occurred: ', e)
            raise Http404
