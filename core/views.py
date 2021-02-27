import requests
from django.shortcuts import render, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from .models import Question, Currency, Text
from registration.models import Profile, Seller
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from .forms import ClientForm


# Create your views here.

class HomePageView(ListView):
    model= Text
    context_object_name= "publish"
    template_name = "core/home.html"

class QuestionListView(ListView):
    model= Question
    context_object_name= "questions"
    template_name = "core/about.html"
    

def panel(request, user_id):
    client= Profile.objects.get(user=user_id)
    seller= Seller.objects.all()
    url= 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data=requests.get(url).json()
    return render(request, "core/panel.html",{'data':data, 'client':client})


def seller(request, user_id):
    seller= Seller.objects.get(user=user_id)
    clients = Profile.objects.all()
    return render(request, "core/seller.html",{'seller': seller, 'clients':clients})

# Modal de creación de nuevo cliente
class RegistrarUsuario(CreateView):
    model= Profile
    form_class= ClientForm
    template_name='core/registrar_usuario.html'

    def post(self, request, *args, **kwargs):
        form= self.form_class(request.POST)
        if form.isvalid():
            nuevo_cliente= Profile(
            user= form.cleaned_data.get('user'),
            days= form.cleaned_data.get('days'),
            start= form.cleaned_data.get('start'),
            money= form.cleaned_data.get('money'),
            currencys= form.cleaned_data.get('currencys'),
            phone= form.cleaned_data.get('phone'),
            seller= form.cleaned_data.get('seller'),
            client_active= form.cleaned_data.get('client_active'),
            paybutton= form.cleaned_data.get('paybutton'),
            urlbutton= form.cleaned_data.get('urlbutton'),
            )
            nuevo_cliente.save()
            return redirect('core/seller')
        else:
            return render (request, self.template_name, {'form':form})


#Errors Views
class Error404View(TemplateView):
    template_name = "core/error.html"

class Error505View(TemplateView):
    template_name = "core/error.html"

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view