import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View

from .cart import Cart
from product_module.models import ProductModel
from .models import *


def cart_summery(request):
    try:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = {}
        total_summery = 0
        for product_id in cart.cart.keys():
            product = ProductModel.objects.filter(id=product_id).first()
            total = int(product.price)*cart.cart[product_id]
            totals[product_id] = total
            total_summery += total

        return render(request, 'cart_summery.html', {
            'cart_products': cart_products,
            'quantities': quantities,
            'totals': totals,
            'total': total_summery
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')
        return redirect('error')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(ProductModel, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(ProductModel, id=product_id)
        cart.update(product=product, quantity=product_qty)
        return redirect('cart_summery')


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(ProductModel, id=product_id)
        cart.remove(product=product)
        return redirect('cart_summery')


class InvoiceView(View):
    def get(self, request):
        try:
            cart = Cart(request)
            cart_products = cart.get_prods()
            quantities = cart.get_quants()
            totals = {}
            total_summery = 0
            for product_id in cart.cart.keys():
                product = ProductModel.objects.filter(id=product_id).first()
                total = int(product.price) * cart.cart[product_id]
                totals[product_id] = total
                total_summery += total

            return render(request, 'invoice.html', {
                'cart_products': cart_products,
                'quantities': quantities,
                'totals': totals,
                'total': total_summery
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')

    def post(self, request):
        try:
            cart = Cart(request)
            cart_products = cart.get_prods()
            quantities = cart.get_quants()
            new_invoice = InvoiceModel.objects.create(user=request.user)
            for product in cart_products:
                for key, value in quantities.items():
                    print(product.id, key, value)
                    if int(key) == int(product.id):
                        new_invoice_product = InvoiceProductModel.objects.create(product=product, number=int(value))
                        new_invoice_product.reduce()
                        new_invoice.products.add(new_invoice_product)
                        new_invoice.save()

            for product in cart_products:
                cart.remove(product=product)

            return redirect('cart_summery')

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')
