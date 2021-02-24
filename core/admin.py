from django.contrib import admin
from .models import Question, Currency, Text

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields= ('id',)
    verbose_name= "Preguntas frencuentes"
    list_display= ('title', 'order', 'updated')


class CurrencyAdmin(admin.ModelAdmin):
    verbose_name= "Criptomonedas"


class TextAdmin(admin.ModelAdmin):
    verbose_name= "Publicidad"
    list_display= ('title', 'order')

admin.site.register(Text, TextAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Currency, CurrencyAdmin)

# Admin Configuration
admin.site.site_header = "Administración Go Money Planet"
admin.site.site_title = "Staff Go Money Planet"

