from django.urls import path
from product_module.views import *

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path('product_list/<slug>/', ProductView.as_view(), name='products'),
    path('product_details/<slug>/', ProductDetailsView.as_view(), name='product_details')
]
