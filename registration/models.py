from django.db import models
from django.contrib.auth.models import User
from core.models import Currency, Plan
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils import timezone

# Delete wallet
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.wallet.delete()
    return 'profiles/' + filename

# Models 
    
class Seller(models.Model):
    user = models.ForeignKey(User, verbose_name= "Nombre de usuario", on_delete=models.CASCADE, null=True, blank=True)
    phone= models.IntegerField(verbose_name= "Teléfono", default=None, null=True, blank=True)
    seller_active = models.BooleanField(default=False, verbose_name= "Vendedor activo")
    created= models.DateField(verbose_name= "Fecha de ingreso", default=None, null=True, blank=True)

    class Meta:
        verbose_name= "Vendedor"
        verbose_name_plural= "Vendedores"
        ordering = ['created']
    
    def __str__(self):
        person= self.user.first_name + ' ' + self.user.last_name
        return person
    
    def email(self):
        return self.user.email
    
    def Nombre(self):
        return self.user.first_name

    def Apellido(self):
        return self.user.last_name


class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    days= models.IntegerField(verbose_name= "Días contrato", null=True, blank=True)
    start = models.DateField(verbose_name= "Fecha de inicio", default=None, null=True, blank=True)
    money = models.IntegerField(verbose_name= "Dinero invertido", default=None, null=True, blank=True)
    gain= models.IntegerField(verbose_name= "Ganancia acumulada", default=None, null=True, blank=True)
    currencys= models.ForeignKey(Currency, verbose_name= "Moneda elegida ", on_delete=models.CASCADE, null=True, blank=True)
    #plan= models.ForeignKey(Plan, verbose_name= "Plan elegido", on_delete=models.CASCADE, null=True, blank=True)
    phone= models.IntegerField(verbose_name= "Teléfono", default=None, null=True, blank=True)
    seller= models.ForeignKey(Seller, verbose_name= "Vendedor asignado", on_delete=models.CASCADE, null=True, blank=True)
    client_active = models.BooleanField(default=False, verbose_name= "Cliente activo")

    class Meta:
        verbose_name= "Perfil Cliente"
        verbose_name_plural="Perfiles de Clientes"
        ordering = ['money']
       
    def __str__(self):
        person= self.user.first_name + ' ' + self.user.last_name
        return person
    
    def Nombre(self):
        return self.user.first_name

    def Apellido(self):
        return self.user.last_name

    def email(self):
        return self.user.email
    




