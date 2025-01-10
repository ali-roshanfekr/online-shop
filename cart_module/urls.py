from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_summery, name='cart_summery'),
    path('add/', cart_add, name='cart_add'),
    path('delete/', cart_delete, name='cart_delete'),
    path('update/', cart_update, name='cart_update'),
]
