import requests
from django.shortcuts import render, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from .models import Question, Currency, Text, Plan
from registration.models import Profile, Seller
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date
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

def plan(request):
    plans= Plan.objects.all()
    
    #n1= plan.invertion
    #n2= plan.percent
    #result= n1 * n2 /100
    return render(request, "core/plan.html",{'plans':plans})    

def panel(request, user_id):
    client= Profile.objects.get(user=user_id)
    f1= client.start
    add=(f1.month)+2
    f3=f1.replace(month=add)
    f2=date.today() 
    days= f3-f2

    days=days.days
    url= 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data=requests.get(url).json()
    return render(request, "core/panel.html",{'data':data, 'client':client, 'days':days})


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
        if request.is_ajax():            
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
                mensaje= f'{self.model.__name__} registrado correctamente'
                error= 'no hay error!'
                response= JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code= 201 #creado
                return response                
            else:
                mensaje= f'{self.model.__name__} no se ha podido registrar'
                error= form.errors
                response= JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code= 400 #errores del cliente
                return response   
        else:
            return redirect('home')

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