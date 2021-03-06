from django.contrib import admin
from .models import Profile, Seller, User


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    verbose_name= "Tablero del usuario"
    #readonly_fields= ('user', 'wallet')
    list_display = ['Nombre', 'Apellido', 'meses','inversion','currency', 'gain', 'start', 'finaliza', 'phone', 'email', 'seller',]

class SellerAdmin(admin.ModelAdmin):
    verbose_name= "Vendedor"
    #readonly_fields= ('created',)
    list_display= ('Nombre', 'Apellido', 'user', 'phone', 'email', 'created')
 
 
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Seller, SellerAdmin)


