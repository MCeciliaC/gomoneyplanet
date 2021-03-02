from django.db import models
from django.contrib.auth.models import User
from core.models import Currency, Plan
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import date, timedelta


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    start = models.DateField(verbose_name= "Fecha de inicio", auto_now_add=True)
    gain= models.IntegerField(verbose_name= "Ganancia", default=None, null=True, blank=True)
    currency= models.ForeignKey(Currency, on_delete=models.PROTECT, verbose_name= "Moneda principal", null=True, blank=True)
    plan= models.ForeignKey(Plan, verbose_name= "Plan elegido", on_delete=models.CASCADE)
    phone= models.IntegerField(verbose_name= "Teléfono", default=None, null=True, blank=True)
    seller= models.ForeignKey(Seller, verbose_name= "Vendedor asignado", on_delete=models.CASCADE)
    client_active = models.BooleanField(default=False, verbose_name= "Cliente activo")

    class Meta:
        verbose_name= "Perfil Cliente"
        verbose_name_plural="Perfiles de Clientes"
        ordering = ['seller']
       
    def __str__(self):
        person= self.user.first_name + ' ' + self.user.last_name
        return person
    
    def Nombre(self):
        return self.user.first_name

    def Apellido(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def meses(self):
        return self.plan.time
    
    def inversion(self):
        return self.plan.invertion

    def finaliza(self):
        f1= self.start
        plan= self.plan.time

        if plan == 3:
            tres= f1 + timedelta(365/4)
            return tres
        elif plan == 6:
            seis= f1 + timedelta(365/2)
            return seis
        else:
            doce= f1 + timedelta(365)
            return doce

