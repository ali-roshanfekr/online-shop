from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *


# Create your views here.

brand_title = None

class ProductView(View):
    def get(self, request, slug):
        category = CategoryModel.objects.filter(slug=slug).first()
        if brand_title is not None:
            brand = BrandModel.objects.filter(title=brand_title).first()
            products = ProductModel.objects.filter(category=category, brand=brand)
        else:
            products = ProductModel.objects.filter(category=category)

        paginator = Paginator(products, 2)
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

    def post(self, request, slug):
        global brand_title

        category = CategoryModel.objects.filter(slug=slug).first()
        brand_title = request.POST['brand']
        brand = BrandModel.objects.filter(title=brand_title).first()
        if brand is not None:
            products = ProductModel.objects.filter(category=category, brand=brand)
        else:
            products = ProductModel.objects.filter(category=category)
        paginator = Paginator(products, 2)
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

class CategoryView(View):
    def get(self, request):
        categories = CategoryModel.objects.all()
        return render(request, 'category.html', {
            'categories': categories
        })

class ProductDetailsView(View):
    def get(self, request, slug):
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
