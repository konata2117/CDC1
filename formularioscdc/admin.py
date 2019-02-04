from django.contrib import admin
from .models import Formulario, Pregunta,Respuesta, Proveedor, Comuna, Rol,Realiza,ParaPregunta
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
import xlsxwriter


def Generar_pdf(modeladmin,request,queryset):
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition']= 'filename= qr.rol.pdf'
    buffer =BytesIO()
    c= canvas.Canvas(buffer)
    for qs in queryset:
        nombre = qs.proveedor
        id= qs.id
        fecha= qs.created_date
        fecha1=str(fecha)
        d=fecha1.split(' ')
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
    c.drawString(385,665,d[0])
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

def Generar_excel(modeladmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    print (queryset[0])
    response['Content-Disposition']= 'filename= query.xlsx'
    writer = xlsxwriter.Workbook(response)
    worksheet = writer.add_worksheet()
    for qs in queryset:
        nombre = qs.proveedor
        id= qs.id
        fecha= qs.created_date
        fecha1=str(fecha)
        d=fecha1.split(' ')
        predio=qs.predio
        id_proveedor=qs.proveedor_id
    # Obtener los objetos que deseas exportar e iterar

    #for objeto in queryset:

    worksheet.write('A1',"ID")
    worksheet.write('B1',"NOMBRE")
    worksheet.write('C1',"RUT")
    worksheet.write('A2',str(id))
    worksheet.write('B2',str(nombre))
    worksheet.write('C2',str(predio))
    writer.close()

    return response

def indicadores():
    preguntas=Pregunta.objects.all()
    list = []
    pregunt={}
    cate={}
    nom=[] # creo una lista que va a contener los nombres de las categorias
    nom.append("unouno")
    nom.append("unodos")
    nom.append("unotres")
    nom.append("unocuatro")
    nom.append("unocinco")
    nom.append("unoseis")
    nom.append("unosiete")
    nom.append("unoocho")
    nom.append("unonueve")
    nom.append("unodiez")
    nom.append("unoonce")
    nom.append("unodoce")
    nom.append("unotrece")
    nom.append("unocatorce")
    nom.append("unoquince")
    nom.append("unodieciseis")
    nom.append("unodiecisiete")
    nom.append("unodieciocho")
    nom.append("unodiecinueve")
    nom.append("unoveinte")
    nom.append("unoveintiuno")
    nom.append("dosuno")
    nom.append("dosdos")
    nom.append("dostres")
    nom.append("tres")
    nom.append("tresuno")
    nom.append("tresdos")
    nom.append("trestres")
    nom.append("trescuatro")
    nom.append("trescinco")
    nom.append("tresseis")
    nom.append("cuatro")
    nom.append("cinco")
    #print ("nom: ", nom)

    numero=preguntas.count()
    #print (preguntas[0])
    for i in range(numero):
        cate[preguntas[i]]=[]
    for i in range(numero): #obtengo un un diccionario con una lista de los valores de las categorias
        cate[preguntas[i]].append(preguntas[i].unouno)
        cate[preguntas[i]].append(preguntas[i].unodos)
        cate[preguntas[i]].append(preguntas[i].unotres)
        cate[preguntas[i]].append(preguntas[i].unocuatro)
        cate[preguntas[i]].append(preguntas[i].unocinco)
        cate[preguntas[i]].append(preguntas[i].unoseis)
        cate[preguntas[i]].append(preguntas[i].unosiete)
        cate[preguntas[i]].append(preguntas[i].unoocho)
        cate[preguntas[i]].append(preguntas[i].unonueve)
        cate[preguntas[i]].append(preguntas[i].unodiez)
        cate[preguntas[i]].append(preguntas[i].unoonce)
        cate[preguntas[i]].append(preguntas[i].unodoce)
        cate[preguntas[i]].append(preguntas[i].unotrece)
        cate[preguntas[i]].append(preguntas[i].unocatorce)
        cate[preguntas[i]].append(preguntas[i].unoquince)
        cate[preguntas[i]].append(preguntas[i].unodieciseis)
        cate[preguntas[i]].append(preguntas[i].unodieciocho)
        cate[preguntas[i]].append(preguntas[i].unodiecinueve)
        cate[preguntas[i]].append(preguntas[i].unoveinte)
        cate[preguntas[i]].append(preguntas[i].unoveintiuno)
        cate[preguntas[i]].append(preguntas[i].dosuno)
        cate[preguntas[i]].append(preguntas[i].dosdos)
        cate[preguntas[i]].append(preguntas[i].dostres)
        cate[preguntas[i]].append(preguntas[i].tres)
        cate[preguntas[i]].append(preguntas[i].tresuno)
        cate[preguntas[i]].append(preguntas[i].tresdos)
        cate[preguntas[i]].append(preguntas[i].trestres)
        cate[preguntas[i]].append(preguntas[i].trescuatro)
        cate[preguntas[i]].append(preguntas[i].trescinco)
        cate[preguntas[i]].append(preguntas[i].tresseis)
        cate[preguntas[i]].append(preguntas[i].cuatro)
        cate[preguntas[i]].append(preguntas[i].cinco)


    for i in range(numero): #obtengo los indicadores de las preguntas que se van a realizar
        pregunt[preguntas[i]]=[]
        for j in range(32):

            if cate[preguntas[i]][j]==True:
                pregunt[preguntas[i]].append(nom[j])

    #print (pregunt)
    return pregunt
def riesgos():
    comunas=Comuna.objects.all()
    list = []
    comun={}
    riesgo={}
    nom=[] # creo una lista que va a contener los nombres de las categorias
    nom.append("unouno")
    nom.append("unodos")
    nom.append("unotres")
    nom.append("unocuatro")
    nom.append("unocinco")
    nom.append("unoseis")
    nom.append("unosiete")
    nom.append("unoocho")
    nom.append("unonueve")
    nom.append("unodiez")
    nom.append("unoonce")
    nom.append("unodoce")
    nom.append("unotrece")
    nom.append("unocatorce")
    nom.append("unoquince")
    nom.append("unodieciseis")
    nom.append("unodiecisiete")
    nom.append("unodieciocho")
    nom.append("unodiecinueve")
    nom.append("unoveinte")
    nom.append("unoveintiuno")
    nom.append("dosuno")
    nom.append("dosdos")
    nom.append("dostres")
    nom.append("tres")
    nom.append("tresuno")
    nom.append("tresdos")
    nom.append("trestres")
    nom.append("trescuatro")
    nom.append("trescinco")
    nom.append("tresseis")
    nom.append("cuatro")
    nom.append("cinco")
    #print ("nom: ", nom)

    numero=comunas.count()
    #print (preguntas[0])
    for i in range(numero):
        comun[comunas[i]]=[]
    for i in range(numero): #obtengo un un diccionario con una lista de los valores de las categorias
        comun[comunas[i]].append(comunas[i].unouno)
        comun[comunas[i]].append(comunas[i].unodos)
        comun[comunas[i]].append(comunas[i].unotres)
        comun[comunas[i]].append(comunas[i].unocuatro)
        comun[comunas[i]].append(comunas[i].unocinco)
        comun[comunas[i]].append(comunas[i].unoseis)
        comun[comunas[i]].append(comunas[i].unosiete)
        comun[comunas[i]].append(comunas[i].unoocho)
        comun[comunas[i]].append(comunas[i].unonueve)
        comun[comunas[i]].append(comunas[i].unodiez)
        comun[comunas[i]].append(comunas[i].unoonce)
        comun[comunas[i]].append(comunas[i].unodoce)
        comun[comunas[i]].append(comunas[i].unotrece)
        comun[comunas[i]].append(comunas[i].unocatorce)
        comun[comunas[i]].append(comunas[i].unoquince)
        comun[comunas[i]].append(comunas[i].unodieciseis)
        comun[comunas[i]].append(comunas[i].unodieciocho)
        comun[comunas[i]].append(comunas[i].unodiecinueve)
        comun[comunas[i]].append(comunas[i].unoveinte)
        comun[comunas[i]].append(comunas[i].unoveintiuno)
        comun[comunas[i]].append(comunas[i].dosuno)
        comun[comunas[i]].append(comunas[i].dosdos)
        comun[comunas[i]].append(comunas[i].dostres)
        comun[comunas[i]].append(comunas[i].tres)
        comun[comunas[i]].append(comunas[i].tresuno)
        comun[comunas[i]].append(comunas[i].tresdos)
        comun[comunas[i]].append(comunas[i].trestres)
        comun[comunas[i]].append(comunas[i].trescuatro)
        comun[comunas[i]].append(comunas[i].trescinco)
        comun[comunas[i]].append(comunas[i].tresseis)
        comun[comunas[i]].append(comunas[i].cuatro)
        comun[comunas[i]].append(comunas[i].cinco)


    for i in range(numero): #obtengo los indicadores de las preguntas que se van a realizar
        riesgo[comunas[i]]=[]
        for j in range(32):

            if comun[comunas[i]][j]==True:
                riesgo[comunas[i]].append(nom[j])

    #print (riesgo)
    return riesgo
def actualizar(modeladmin,request,queryset):
    Realiza.objects.all().delete()
    preguntas=se_realiza()
    comuna=Comuna.objects.all()
    for i in range(len(preguntas)):
        for j in range(len(preguntas[comuna[i]])):
            tt=list(preguntas[comuna[i]])
            add=Realiza.objects.create(comuna=str(comuna[i]), pregunta=str(tt[j]))
            add.save()
def se_realiza():
    comunas=riesgos()
    comu=Comuna.objects.all()
    pregun=Pregunta.objects.all()
    preguntas=indicadores()

    co={}
    for i in range (len(comunas)):
        co[comu[i]]=set()


    for i in range(len(comunas)):
        #print (len(comunas[comu[i]]))
        for j in range(len(comunas[comu[i]])):
            for x in range(len(preguntas)):
                for ss in range(len(preguntas[pregun[x]])):
                    cosa=preguntas[pregun[x]][ss]
                    if cosa == comunas[comu[i]][j]:
                        co[comu[i]].add(pregun[x])
                        #print("true: ", cosa, pregun[x], comu[i])
                        break
                        #lis.append(cosa)



    return co
class ChoiceInline(admin.StackedInline):
    model = ParaPregunta
    extra = 9
    

class REa(admin.ModelAdmin):

    list_display=('comuna','pregunta')
    search_fields=('comuna','pregunta',)
    actions=[actualizar]
class FormularioAd(admin.ModelAdmin):
    preguntas=se_realiza()
    #print(preguntas)
    def preguntas(self,obj):
        print(obj.comuna)
        pregunta=Realiza.objects.filter(comuna=obj.comuna)
        print (pregunta)
        for i in pregunta:
           print (i.pregunta)
           return  i.pregunta
  
    list_display=('id','rol','comuna','predio','proveedor','encargado','created_date','imagen','preguntas')
    readonly_fields=('preguntas','pregunta',)
    fieldsets=[
       ('Información Personal', {'fields':['encargado','proveedor','comuna','rol','predio','imagen']}),
        ('Medidas de Control', {'fields':['preguntas','respuesta']}),
    ]
    actions= [Generar_pdf,Generar_excel]
    search_fields=('id','predio',)
    #inlines=[ChoiceInline,]
    def save(self,*args,**kwargs):
        self.field3= self.preguntas()
        super(Formulario,self).save(*args,**kwargs)
    #inlines=[ChoiceInline]
class Comu(admin.ModelAdmin):
      list_display=('comuna', 'unouno','unodos',
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
'cinco')
class Predios(admin.ModelAdmin):
    list_display=('rol','proveedor')
    search_fields=('rol','proveedor',)
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
'cinco','tipo')
class Provee(admin.ModelAdmin):
    list_display=('nombre','rut')
    search_fields=('nombre','rut',)
  #inlines=[ChoiceInline]
admin.site.register(Formulario, FormularioAd)


admin.site.register(Pregunta,Pre)
admin.site.register(Respuesta)
admin.site.register(Proveedor,Provee)
admin.site.register(Comuna,Comu)
admin.site.register(Rol,Predios)
admin.site.register(Realiza,REa)