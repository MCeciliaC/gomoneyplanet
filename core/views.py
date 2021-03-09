import requests
from django.shortcuts import render, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Question, Currency, Text, Plan
from registration.models import Profile, Seller
from datetime import datetime
from datetime import date, timedelta
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

class PlanView(ListView):
    model= Plan
    context_object_name= "plans"
    template_name = "core/plan.html"

def panel(request, user_id):
    client= Profile.objects.get(user=user_id)
    # Días restantes:
    f1= client.start
    f2=date.today() 
    plan= client.plan.time
    if plan == 3:
        fin= f1 + timedelta(365/4)        
    elif plan == 6:
        fin= f1 + timedelta(365/2)  
    else:
        fin= f1 + timedelta(365)  
    days= fin - f2
    days=days.days
    #Api Criptos
    url= 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data=requests.get(url).json()
    return render(request, "core/panel.html",{'data':data, 'client':client, 'days': days})

#Panel de vendedores con sus clientes 
class SellerView(ListView):
    model= Profile
    context_object_name= "clients"
    template_name = "core/seller.html"

# Crear nuevo cliente
class ClientCreate(CreateView):
    model= Profile
    form_class= ClientForm  
    template_name = "core/create.html"

    def get_success_url(self):
        return reverse_lazy('seller') + '?created' 

class ClientUpdate(UpdateView):
    model= Profile
    form_class= ClientForm  
    template_name = "core/update.html"

    def get_success_url(self):
        return reverse_lazy('seller') + '?ok'  

class ClientDelete(DeleteView):
    model= Profile
    template_name = "core/confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('seller') + '?deleted'  


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