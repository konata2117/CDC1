from django.contrib import admin
from django.contrib.auth.models import User
from .models import Formulario, Pregunta,RespuestaBinaria, Proveedor, Comuna, Rol,Realiza
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
import xlsxwriter
from django import forms

def Generar_Reporte(modeladmin,request,queryset):
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
def Generar_Formulario(modeladmin,request,queryset):
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
        encargado=qs.encargado_id
        rol=qs.rol_id
        comuna=qs.comuna_id
    preguntas=Realiza.objects.filter(comuna=comuna)
    rut_proveedor=Proveedor.objects.get(id=id_proveedor)
    encargado_id=User.objects.get(id=encargado)
    roles=Rol.objects.get(id=rol)
    comunas=Comuna.objects.get(comuna=comuna)
    print(encargado_id)
    c.setFont("Helvetica",7)
    c.drawImage("imagenes/arauco.jpg",60,740,100,100,preserveAspectRatio=True)
    text=c.beginText(180,750)
    
    text.textLines("FORMULARIO DE REVISION DE MEDIDAS PREVENTIVAS Y DE CONTROL")
    c.drawText(text)
    text1=c.beginText(250,735)
    text1.textLine("MADERAS CONTROLADAS")
    c.drawText(text1)
    c.line(60,730,565,730)
    c.drawString(200,690,"FECHA")
    c.rect(195,680,50,25)
    c.rect(245,705,80,20)
    c.drawString(250,710,"EVAL. INICIAL")                                         
    c.rect(245,680,80,25)
    c.rect(325,680,80,25)
    c.rect(405,680,80,25)
    c.rect(485,680,80,25)
    c.rect(325,705,80,20)
    c.drawString(350,710,"1a VISITA")
    c.drawString(430,710,"2a VISITA")
    c.drawString(510,710,"3a VISITA")
    c.drawString(260,690,d[0])
    c.rect(405,705,80,20)
    c.rect(485,705,80,20)
    c.drawString(65,660,"PROVEEDOR: ")
    c.drawString(330,660,"RUT PROVEEDOR: ")
    c.rect(60,655,265,20)
    c.drawString(65,640,"NOMBRE PREDIO/DIRECCIÓN: ")
    c.drawString(200,640,str(predio))
    c.drawString(330,640,"ROL/N°: ")
    c.drawString(380,640,str(roles))
    c.drawString(430,640,"COMUNA: ")
    c.drawString(470,640,str(comunas))
    c.rect(325,655,240,20)
    c.rect(325,635,240,20)
    c.rect(60,635,265,20)
    c.rect(60,615,135,20)
    c.drawString(65,620,"CAT. RIESGO FSC: ")
    c.line(130,635,130,615)
    c.drawString(135,620,"1")
    c.line(145,635,145,615)
    c.drawString(150,620,"2")
    c.line(160,635,160,615)
    c.drawString(165,620,"3")
    c.line(175,635,175,615)
    c.drawString(180,620,"BR")
    c.rect(325,615,240,20)
    c.drawString(330,620,"ENC. DE CONTROL: ")
    c.drawString(420,620,str(encargado_id))
    c.drawString(425,660,str(rut_proveedor.rut))
    c.drawString(135,660,str(nombre))
    preg=c.beginText(65,590)
    count=0
    for i in preguntas:
        preg.textLines(str(i.pregunta))
        count=1+count
        
        preg.textLines("\n\n\n\n")
        #if count>7:
         #   c.showPage()
          #  count=0
    c.drawText(preg)
    
    c.showPage()
    c.save()
    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
    
def res_pre():
    preguntas=Pregunta.objects.filter(tipo='BINARIA')
    #for i in preguntas:
     #   print (i.pregunta) 
    

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


class REa(admin.ModelAdmin):

    list_display=('comuna','pregunta')
    search_fields=('comuna','pregunta',)
    actions=[actualizar]
class ForForm(forms.ModelForm):

    class Meta:
        model = Formulario
        fields = "__all__" 
    def __init__(self, *args, **kwargs):
        super(ForForm, self).__init__(*args, **kwargs)
        self.fields['pregunta'].queryset = Realiza.objects.filter(comuna=self.instance.comuna)
class FormularioAd(admin.ModelAdmin):
    #preguntas=se_realiza()
    #print(preguntas)
    res_pre()
    form = ForForm
    def preguntas(self,obj):
        #print(obj.comuna)
        pregunta=Realiza.objects.filter(comuna=obj.comuna)
        #for p in pregunta:
            #print (p.pregunta)
        #contexto={'preguntas':pregunta}
        #return render(request,'admin/prueba.html',contexto)
  
    list_display=('id','rol','comuna','predio','proveedor','encargado','created_date','imagen')
    readonly_fields=('preguntas',)
    fieldsets=[
       ('Información Personal', {'fields':['encargado','proveedor','comuna','rol','predio','imagen']}),
        ('Medidas de Control', {'fields':['pregunta','respuesta','comentario']}),
    ]
    actions= [Generar_Reporte,Generar_Formulario]
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


admin.site.register(Comuna,Comu)
admin.site.register(Pregunta,Pre)
admin.site.register(Realiza,REa)
admin.site.register(Proveedor,Provee)
admin.site.register(Rol,Predios)
admin.site.register(RespuestaBinaria)
admin.site.register(Formulario, FormularioAd)