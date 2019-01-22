from django.contrib import admin
from .models import Formulario, Pregunta,Respuesta, Proveedor, Comuna, Rol,Realiza
from .resources import FormularioResource
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
#dataset=FormularioResource().export()
class Froe(admin.ModelAdmin):
    fieldsets=[
        ('Información Personal', {'fields':['encargado','proveedor','rol','comuna']}),
        
   ]
   #search_fields=['pregunta','comuna']
   #list_filter=['pregunta','comuna']
class ChoiceInline(admin.TabularInline):
    model =Pregunta
class FormularioAdmin(admin.ModelAdmin):
    #def get_user_link(self,obj):
       #return  <a>< href="admin/formularioscdc/formulario/ + 'str(obj.id)+' "class="detail_user"> PDF</a>
    #get_user_link.short_description= 'Formulario'
    #get_user_link.allow_tags=True    
    list_display=('id','rol','proveedor','encargado','created_date','imagen')
   # some_view(request.POST)
    fieldsets=[
        ('Información Personal', {'fields':['encargado','proveedor','comuna','rol','predio','imagen']}),
        ('Medidas de Control', {'fields':['pregunta','respuesta']}),
    ]

class FormularioAdmin(ImportExportModelAdmin):
        resource_class=FormularioResource
class FormularioAdmin(ImportExportActionModelAdmin):
    pass
#formulario_resource = FormularioResource()
#dataset=formulario_resource.export()
#print(dataset.csv)
#class PDF(PDFTemplateView):
 #   filename='prueba.pdf'
  #  template_name="prueba.html"

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
admin.site.register(Formulario, FormularioAdmin)    
#admin.site.register(Formulario,Froe)

admin.site.register(Pregunta,Pre)
admin.site.register(Respuesta)
admin.site.register(Proveedor)
admin.site.register(Comuna)
# Register your models here.
admin.site.register(Rol,Predios)
#admin.site.register(Realiza,PDF)
