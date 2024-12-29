from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='blog_view'),
]
