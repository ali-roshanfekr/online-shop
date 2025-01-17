from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('error/', ErrorView.as_view(), name='error'),
    path('user-exit/', UserExit.as_view(), name='user-exit'),
]
