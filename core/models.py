from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Models Question, Month, Plan, Currency, Text, Social
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

class Plan(models.Model):
    id= models.AutoField(primary_key=True, verbose_name= "Id")
    name= models.CharField(max_length=100, verbose_name= "Nombre", null=True, blank=True)
    invertion= models.IntegerField(verbose_name= "Inversión inicial", null=True, blank=True)
    time= models.IntegerField(verbose_name= "Duración en meses", null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name= "name", null=True, blank=True)
    percent= models.FloatField(verbose_name="Porcentaje mensual", null=True, blank=True)
    active = models.BooleanField(verbose_name= "Plan activo", default=False)

    class Meta:
        verbose_name= "Plan disponible"
        verbose_name_plural= "Planes disponibles"
        ordering = ['id']
    
    def __str__(self):
        return self.name
        
    def id(self):
        return self.name

    def result(self):
        n1= self.invertion
        n2= self.percent
        n3= self.time
        result= n1 * n2 /100
        result= result * n3
        result= n1 + result
        return result

class Currency(models.Model):
    name= models.CharField(max_length=200, unique=True, verbose_name= "Nombre", null=True, blank=True)

    class Meta:
        verbose_name= "Criptomoneda" 
  
    def __str__(self):
        return self.name

class Text(models.Model):
    id= models.AutoField(primary_key=True, verbose_name= "Id")
    title= models.CharField(max_length=1000, verbose_name= "Título", null=True, blank=True)
    order= models.SmallIntegerField(verbose_name= "Orden", null=True, blank=True)
    text= RichTextField(max_length=1000, verbose_name= "Desarrollo", null=True, blank=True)
    video= models.URLField(verbose_name= "Link a youtube",null=True, blank=True)
    active= models.BooleanField(default=False, verbose_name= "Mostrar")

    class Meta:
        verbose_name= "Publicidad"
        verbose_name_plural= "Publicidades"
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Social(models.Model):
    id= models.AutoField(primary_key=True, verbose_name= "Id")
    title= models.CharField(max_length=100, verbose_name= "Red social")
    link= models.URLField(verbose_name= "Link sitio", default=None, max_length=500, null=True, blank=True)
    tag= models.CharField(max_length=100, verbose_name= "Ícono class=", default='fas fa-redo')
    active= models.BooleanField(default=False, verbose_name= "Mostrar")
    
    class Meta:
        verbose_name= "Red social"
        verbose_name_plural= "Redes sociales"
        ordering = ['title']
    
    def __str__(self):
        return self.title

