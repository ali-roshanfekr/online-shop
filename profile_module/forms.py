from django import forms

from user_module.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'city', 'address', 'postcode')
