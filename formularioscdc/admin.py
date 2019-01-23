from django.contrib import admin
from .models import Formulario, Pregunta,Respuesta, Proveedor, Comuna, Rol,Realiza
from .resources import FormularioResource
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from formularioscdc.views import GeneratePDF
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    
from io import StringIO
from reportlab.platypus import BaseDocTemplate, Paragraph, Frame

def Generar_pdf(modeladmin,request,queryset):
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition']= 'filename= qr.rol.pdf'
    buffer =BytesIO()
    c= canvas.Canvas(buffer)
    for qs in queryset:
        nombre = qs.proveedor
        id= qs.id
        fecha= qs.created_date
        predio=qs.predio
        id_proveedor=qs.proveedor_id
    print (nombre,id,fecha,predio,id_proveedor)
    rut_proveedor=Proveedor.objects.get(id=id_proveedor)
    print (rut_proveedor.rut)
    c.drawImage("imagenes/Arauco-logo.jpg",60,740,100,100,preserveAspectRatio=True)
    c.drawString(170,750,"REPORTE VISITA CONTROL DE COMPRA")
    c.line(60,740,540,740)
    c.rect(60,710,480,23)
    c.drawString(230,715,"DETALLE FORMULARIO")
    c.drawString(60,690,"ID ")
    c.drawString(305,690,"FECHA")
    c.rect(60,660,235,20)
    c.rect(305,660,235,20)
    c.drawString(175,665,str(id))
    c.drawString(345,665,str(fecha))
    c.drawString(60,640,"RUT PROVEEDOR")
    c.drawString(305,640,"PROVEEDOR")
    c.rect(60,610,235,20)
    c.rect(305,610,235,20)
    c.drawString(145,615,str(rut_proveedor.rut))
    c.drawString(345,615,str(nombre))
    c.showPage()
    c.save()
    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
class Froe(admin.ModelAdmin):
    fieldsets=[
        ('Información Personal', {'fields':['encargado','proveedor','rol','comuna']}),
        
   ]
   
class ChoiceInline(admin.TabularInline):
    model =Pregunta
class FormularioAd(admin.ModelAdmin):
     
    list_display=('id','rol','proveedor','encargado','created_date','imagen')
    fieldsets=[
        ('Información Personal', {'fields':['encargado','proveedor','comuna','rol','predio','imagen']}),
        ('Medidas de Control', {'fields':['pregunta','respuesta']}),
    ]
    actions =[Generar_pdf]
class FormularioAdmin(ImportExportModelAdmin):
        resource_class=FormularioResource
        list_display=('id','rol','proveedor','encargado','created_date','imagen')
class FormularioAdmin(ImportExportActionModelAdmin):
    pass

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
admin.site.register(Formulario, FormularioAd)    
admin.site.register(Pregunta,Pre)
admin.site.register(Respuesta)
admin.site.register(Proveedor)
admin.site.register(Comuna)
admin.site.register(Rol,Predios)
