from django import forms
from django.contrib.auth.models import User
from registration.models import Profile, Seller

class ClientForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ['user', 'days', 'start', 'money', 'currencys', 'phone', 'seller', 'client_active']
