from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from favorites_module.favorites import Favorites
from product_module.models import ProductModel


def favorites_add(request):
    favorites = Favorites(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(ProductModel, id=product_id)
        favorites.add(product=product)
        response = JsonResponse({'status': 'success'})
        return response


def favorites_delete(request):
    favorites = Favorites(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(ProductModel, id=product_id)
        favorites.remove(product=product)
        response = JsonResponse({'status': 'success'})
        return response
