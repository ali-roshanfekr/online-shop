import logging
import os.path

from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from .forms import ContactForm


# Create your views here.

class ContactView(View):
    def get(self, request):
        try:
            form = ContactForm
            return render(request, 'contact.html', {
                'form': form
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')

    def post(self, request):
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save()
                contact.save()
                return render(request, 'contact.html', {
                    'form': form,
                    'success': True
                })

            else:
                form = ContactForm
                return render(request, 'contact.html', {
                    'form': form,
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')


class UploadView(View):
    def get(self, request):
        try:
            return render(request, 'upload_image.html', {

            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')

    def post(self, request):
        try:
            image = request.FILES['image']
            uploads_dir = os.path.join(settings.MEDIA_ROOT, 'images')
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)

            file_path = os.path.join(uploads_dir, image.name)
            with open(file_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            return render(request, 'upload_image.html', {
                'success': True
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')
