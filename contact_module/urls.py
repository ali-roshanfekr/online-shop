from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('upload/', UploadView.as_view(), name='upload')
]
