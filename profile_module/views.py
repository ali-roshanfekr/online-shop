import logging

from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from cart_module.models import InvoiceModel
from user_module.models import CityModel
from utils.utils import creat_random_code

from .forms import ProfileForm


class ProfileView(View):
    try:
        def get(self, request):
            if request.user.is_authenticated:
                invoice_list = InvoiceModel.objects.all().order_by('-create_at')
                invoices = []
                for invoice in invoice_list[0:2]:
                    if invoice.user == request.user:
                        invoices.append(invoice)
                return render(request, 'profile.html', {
                    'invoices': invoices
                })

            else:
                raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
        raise Http404


class EditProfileView(View):
    try:
        def get(self, request):
            if request.user.is_authenticated:
                user = request.user
                form = ProfileForm(
                    initial={'username': user.username, 'email': user.email, 'phone': user.phone,
                             'address': user.address,
                             'postcode': user.postcode, 'city': user.city})
                return render(request, 'edit_profile.html', {
                    'form': form
                })

            else:
                raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
        raise Http404

    def post(self, request: HttpRequest):
        try:
            form = ProfileForm(request.POST)
            user = request.user
            username = user.username
            user.username = creat_random_code(100)
            user.save()

            if form.is_valid():
                user.username = form['username'].value()
                user.email = form['email'].value()
                user.phone = form['phone'].value()
                user.address = form['address'].value()
                user.postcode = form['postcode'].value()
                city = CityModel.objects.filter(id=form['city'].value()).first()
                user.city = city

                user.save()

                return redirect('profile')

            else:
                user.username = username
                user.save()
                form = ProfileForm(
                    initial={'username': user.username, 'email': user.email, 'phone': user.phone,
                             'address': user.address,
                             'postcode': user.postcode, 'city': user.city})
                return render(request, 'edit_profile.html', {
                    'form': form,
                    'error': True
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error('This is an error message.', e)
            raise Http404


def second_sidebar(request):
    try:
        return render(request, '2nd_sidebar.html', {})

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error('This is an error message.', e)
        raise Http404
