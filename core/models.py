from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Question Model
class Question(models.Model):
    id= models.SmallIntegerField(primary_key=True, verbose_name= "Id")
    order= models.SmallIntegerField(verbose_name= "Orden", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name= "Título") 
    text= RichTextField(max_length=1000, verbose_name= "Desarrollo") 
    updated= models.DateTimeField(auto_now_add = True, verbose_name= "Fecha de creación") 

    class Meta:
        verbose_name= "Pregunta frecuente"
        ordering = ['order']
    
    def __str__(self):
        return self.title

# Currency Model
class Currency(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name= "Moneda") 
    name= models.CharField(max_length=200, verbose_name= "Nombre", null=True, blank=True)

    class Meta:
        verbose_name= "Criptomoneda" 
  
    def __str__(self):
        return self.name

class Text(models.Model):
    id= models.AutoField(primary_key=True, verbose_name= "Id")
    title= models.CharField(max_length=1000, verbose_name= "Título", null=True, blank=True)
    order= models.SmallIntegerField(verbose_name= "Orden", null=True, blank=True)
    text= RichTextField(max_length=1000, verbose_name= "Desarrollo", null=True, blank=True)

    class Meta:
        verbose_name= "Publicidad"
        verbose_name_plural= "Publicidades"
        ordering = ['order']
    
    def __str__(self):
        return self.title

