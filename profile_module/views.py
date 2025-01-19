import os

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from cart_module.models import InvoiceModel
from user_module.models import CityModel
from .forms import ProfileForm
from utils.utils import creat_random_code
from favorites_module.favorites import Favorites

username = None


class ProfileView(View):
    def get(self, request):
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


class EditProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = ProfileForm(initial={
                'username': user.username,
                'phone': user.phone,
                'email': user.email,
                'city': user.city,
                'address': user.address,
                'postcode': user.postcode,
            })
            return render(request, 'edit_profile.html', {
                'form': form
            })

        else:
            raise Http404

    def post(self, request):
        if request.user.is_authenticated:
            global username

            user = request.user
            form = ProfileForm(request.POST)
            username = user.username
            user.username = creat_random_code(50)
            user.save()

            if form.is_valid():
                user.username = form['username'].value()
                user.email = form['email'].value()
                user.phone = form['phone'].value()
                city = CityModel.objects.filter(id=form['city'].value()).first()
                user.city = city
                user.address = form['address'].value()
                user.postcode = form['postcode'].value()
                if 'image' in request.FILES:

                    if user.image:
                        os.remove(user.image.path)
                    user.image = request.FILES['image']

                user.save()

                return redirect('profile')

            else:
                user.username = username
                user.save()

                form = ProfileForm(initial={
                    'username': user.username,
                    'phone': user.phone,
                    'email': user.email,
                    'city': user.city,
                    'address': user.address,
                    'postcode': user.postcode,
                })

                return render(request, 'edit_profile.html', {
                    'form': form,
                    'error': True
                })


def second_sidebar(request):
    return render(request, '2nd_sidebar.html', {

    })


def second_header(request):
    return render(request, '2nd_header.html', {

    })


def scripts(request):
    return render(request, 'scripts.html', {

    })
