from django import forms
from django.contrib.auth.models import User
from registration.models import Profile


class ClientForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ['user', 'currency', 'plan', 'phone', 'seller', 'client_active']
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            #'start': forms.DateInput(attrs={'class':'form-control', 'placeholder':'día/ mes/ año'}),
            'currency': forms.Select(attrs={'class':'form-control'}),
            'plan': forms.Select(attrs={'class':'form-control'}),             
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numero '}),
            'seller': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'user':'Usuario', 'currency': 'Moneda', 'seller': 'Vendedor'
        }