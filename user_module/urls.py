from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('activation_code/', ActivationCode.as_view(), name='activation_code'),
    path('activation_code_forgetpass/', ActivationCodeForgetPass.as_view(), name='activation_code_forgetpass'),
    path('forgetpass/', ForgetPassView.as_view(), name='forgetpass'),
    path('new_password/', NewPassWordView.as_view(), name='new_password'),
    path('logout/', LogOutView.as_view(), name='logout')
]
