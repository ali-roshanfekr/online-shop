from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='blogs'),
    path('blog_details/<id>/', BlogDetailView.as_view(), name='blog_details')
]
