from django.shortcuts import render
from django.views import View
from .models import BlogModel

# Create your views here.


class BlogView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
