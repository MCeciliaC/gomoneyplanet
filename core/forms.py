from django import forms
from django.contrib.auth.models import User
from registration.models import Profile


class ClientForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ['user', 'start', 'currency', 'plan', 'phone', 'seller', 'client_active']
        widgets = {
          
             
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numero '}),
        }
        labels = {
            'user':'Usuario', 'start':'Fecha de incio', 'currency': 'Moneda elegida'
        }
