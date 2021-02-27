from django.contrib import admin
from .models import Question, Plan, Currency, Text, Social

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields= ('id',)
    verbose_name= "Preguntas frencuentes"
    list_display= ('title', 'order', 'updated',)

class PlanAdmin(admin.ModelAdmin):
    verbose_name= "Plan"
    list_display= ('name', 'invertion', 'time', 'percent', 'active', 'result')
    
class CurrencyAdmin(admin.ModelAdmin):
    verbose_name= "Criptomonedas"

class TextAdmin(admin.ModelAdmin):
    verbose_name= "Publicidad"
    list_display= ('title', 'order',)

class SocialAdmin(admin.ModelAdmin):
    verbose_name= "Redes sociales"
    list_display= ('title',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Social, SocialAdmin)

# Admin Configuration
admin.site.site_header = "Administración Go Money Planet"
admin.site.site_title = "Staff Go Money Planet"

