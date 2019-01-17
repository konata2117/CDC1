from django.contrib import admin
from .models import Formulario, Pregunta,Respuesta, Proveedor, Comuna, Rol,Realiza


class Froe(admin.ModelAdmin):
    fieldsets=[
        ('Información Personal', {'fields':['encargado','proveedor','rol','comuna']}),
        
   ]
   #search_fields=['pregunta','comuna']
   #list_filter=['pregunta','comuna']
class ChoiceInline(admin.TabularInline):
    model =Pregunta
class Mostrar(admin.ModelAdmin):

    list_display=('id','rol','proveedor','encargado','created_date','imagen')
    fieldsets=[
        ('Información Personal', {'fields':['encargado','proveedor','comuna','rol','predio','imagen']}),
        ('Medidas de Control', {'fields':['pregunta','respuesta']}),
    ]
class Predios(admin.ModelAdmin):
    list_display=('rol','proveedor')

class Pre(admin.ModelAdmin):
  list_display=('pregunta','id', 'unouno','unodos',
'unotres',
'unocuatro',
'unocinco',
'unoseis',
'unosiete',
'unoocho',
'unonueve',
'unodiez',
'unoonce',
'unodoce',
'unotrece',
'unocatorce',
'unoquince',
'unodieciseis',
'unodiecisiete',
'unodieciocho',
'unodiecinueve',
'unoveinte',
'unoveintiuno',
'dosuno',
'dosdos',
'dostres',
'tres',
'tresuno',
'tresdos',
'trestres',
'trescuatro',
'trescinco',
'tresseis',
'cuatro',
'cinco',
'serealiza','tipo')
  #inlines=[ChoiceInline] 
admin.site.register(Formulario, Mostrar)    
#admin.site.register(Formulario,Froe)

admin.site.register(Pregunta,Pre)
admin.site.register(Respuesta)
admin.site.register(Proveedor)
admin.site.register(Comuna)
# Register your models here.
admin.site.register(Rol,Predios)
admin.site.register(Realiza)