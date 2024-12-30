import os.path
from django.shortcuts import render
from django.views import View
from django.conf import settings
from .forms import ContactForm

# Create your views here.

class ContactView(View):
    def get(self, request):
        form = ContactForm
        return render(request, 'contact.html', {
            'form': form
        })

    def post(self, request):
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


class UploadView(View):
    def get(self, request):
        return render(request, 'upload_image.html', {

        })

    def post(self, request):
        #دریافت فایل تصویری از صفحه html
        image = request.FILES['image']

        #تعیین یک پوشه برای قرار دادن عکس basedir/uploads/images/
        uploads_dir = os.path.join(settings.MEDIA_ROOT, 'images')

        #اگر مسیر وجود نداشت آن را بساز
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        #مسیر فایل تصویر را مشخص کن
        file_path = os.path.join(uploads_dir, image.name)

        #فایل تصویر را باز کن برای خواندن و نوشتن
        with open(file_path, 'wb+') as destination:

            #فایل تصویری دریافت شده را تکه به تکه بخوان و در فایل تصویر جدید بازنویسی کن
            for chunk in image.chunks():
                destination.write(chunk)

        return render(request, 'upload_image.html', {
            'success': True
        })
