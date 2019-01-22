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
    print (queryset[0])
    response['Content-Disposition']= 'filename= qr.rol.pdf'
    buffer =BytesIO()
    c= canvas.Canvas(buffer)
    signfr=Frame(5.1*inch,1.2*inch,2.8*inch,0.44*inch,showBoundary=1)
    story=[]
    doc=BaseDocTemplate(buffer,showBoundary=1, leftMargin=0.1*inch, rightMargin=0.1*inch,topMargin=0.1*inch,bottomMargin=0.1*inch)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Vendana9', fontName='Vendana', fontSize=9))
    
    #for qs in queryset:
    c.drawString(100,100,"esto es una prueba")
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
