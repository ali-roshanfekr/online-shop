from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user-exit/', UserExit.as_view(), name='user-exit'),
    path('error/', ErrorView.as_view(), name='error'),
]
