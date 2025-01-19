from django.urls import path
from .views import *


urlpatterns = [
    path('add/', favorites_add, name='favorites_add'),
    path('delete/', favorites_delete, name='favorites_delete'),
]
