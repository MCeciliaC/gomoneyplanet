from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm #Importamos formularios genericos para que las vistas lo manejen automaticamente
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy #redireccion
from django import forms
from .models import Profile, Seller
from django.shortcuts import render
from django.template.loader import get_template


#Mixin para comprobar si se está logueado
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html' #template donde se crea el form

    def get_success_url(self):
        return reverse_lazy('login') + '?register'   

    def get_form(self, form_class=None): # Obbtenemos el formulario de registro, lo modificamos y retornamos
        form = super(SignUpView, self).get_form()
        # Modificar widgets en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellido'})                  
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form



# PARA CUANDO EDITE CLIENTES Y USUARIOS
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form
