from django.urls import path
from .views import *


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
]
