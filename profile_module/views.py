import logging
import os

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from cart_module.models import InvoiceModel
from .forms import ProfileForm
from favorites_module.favorites import Favorites

username = None


class ProfileView(View):
    def get(self, request):
        try:
            if request.user.is_authenticated:
                favorites = Favorites(request)
                favorite_products = favorites.get_prods()
                invoice_list = InvoiceModel.objects.filter(user=request.user)
                invoices = invoice_list[0:2]
                return render(request, 'profile.html', {
                    'invoices': invoices,
                    'favorite_products': favorite_products,
                })

            else:
                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')


class EditProfileView(View):
    def get(self, request):
        try:
            if request.user.is_authenticated:
                user = request.user
                form = ProfileForm(instance=user)
                return render(request, 'edit_profile.html', {
                    'form': form
                })

            else:
                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')

    def post(self, request):
        try:
            if request.user.is_authenticated:
                global username

                user = request.user
                form = ProfileForm(request.POST or None, instance=user)

                if form.is_valid():
                    form.save()

                    return redirect('profile')

                else:
                    form = ProfileForm(instance=user)

                    return render(request, 'edit_profile.html', {
                        'form': form,
                        'error': True
                    })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')


def second_sidebar(request):
    return render(request, '2nd_sidebar.html', {

    })


def second_header(request):
    return render(request, '2nd_header.html', {

    })


def scripts(request):
    return render(request, 'scripts.html', {

    })
