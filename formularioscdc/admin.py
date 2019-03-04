from django.contrib import admin
from django.contrib.auth.models import User
from .models import Formulario, Pregunta, Proveedor, Comuna, Rol,Realiza,Pregs
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from django import forms

from reportlab.platypus import Paragraph, Frame, KeepInFrame


from reportlab.lib.styles import ParagraphStyle
def Generar_Formulario(modeladmin,request,queryset):
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition']= 'filename= qr.rol.pdf'

    buffer =BytesIO()
    c= canvas.Canvas(buffer)
    for qs in queryset:
        nombre = qs.proveedor
        id= qs.id
        fecha= qs.eval_inicial
        fecha1=str(fecha)
        d=fecha1.split(' ')
        predio=qs.predio
        final=qs.eval_final
        final1=str(final)
        dd=final1.split(' ')
        id_proveedor=qs.proveedor_id
        encargado=qs.encargado_id
        rol=qs.rol_id
        comuna=qs.comuna_id
    nom=Proveedor.objects.get(rut=nombre)
        #respuesta_id=qs.respuesta_id
    #respuestas=Asociada.objects.get(id=respuesta_id)
    resp=Pregs.objects.filter(formulario_id_id=id)
    preguntas=Realiza.objects.filter(comuna=comuna)
    rut_proveedor=Proveedor.objects.get(id=id_proveedor)
    encargado_id=User.objects.get(id=encargado)
    roles=Rol.objects.get(id=rol)
    #preg=Pregunta.objects.get(id=respuestas.pregunta_id)
    comunas=Comuna.objects.get(comuna=comuna)
    print(encargado_id)
    c.setFont("Helvetica",7)
    c.drawImage("imagenes/Arauco-logo.jpg",60,740,100,100,preserveAspectRatio=True)
    text=c.beginText(180,750)

    text.textLines("FORMULARIO DE REVISIÓN DE MEDIDAS PREVENTIVAS Y DE CONTROL")
    c.drawText(text)
    text1=c.beginText(250,735)
    text1.textLine("MADERAS CONTROLADAS")
    c.drawText(text1)
    c.line(60,730,565,730)
    c.drawString(250,690,"FECHA")
    c.rect(245,680,50,25)
    c.rect(295,705,135,20)
    c.rect(295,680,135,25)
    c.drawString(340,710,"EVAL. INICIAL")
    c.rect(430,705,135,20)
    c.rect(430,680,135,25)
    c.drawString(465,710,"EVAL. FINAL")
    c.drawString(340,690,d[0])
    c.drawString(465,690,dd[0])
    c.drawString(65,660,"PROVEEDOR: ")
    c.drawString(330,660,"RUT PROVEEDOR: ")
    c.rect(60,655,265,20)
    c.drawString(65,640,"NOMBRE PREDIO/DIRECCIÓN: ")
    c.drawString(170,640,str(predio))
    c.drawString(330,640,"ROL/N°: ")
    c.drawString(380,640,str(roles))
    c.drawString(430,640,"COMUNA: ")
    c.drawString(470,640,str(comunas))
    c.rect(325,655,240,20)
    c.rect(325,635,240,20)
    c.rect(60,635,265,20)
    c.rect(325,615,240,20)
    c.drawString(330,620,"ENC. DE CONTROL: ")
    c.drawString(420,620,str(encargado_id))
    c.drawString(425,660,str(rut_proveedor.rut))
    c.drawString(115,660,str(nom.nombre))
    c.rect(490,575,75,20)
    c.drawString(505,580,"SEGUIMIENTO")

    style = ParagraphStyle(
        name='Normal',
        fontName="Helvetica",
        fontSize=8,
    )

    count=475
    tt = 0
    r=1
    w=1
    for i in resp:
        frame12 = Frame(60,count,505,100)
        s2 = str(r)
        story222 = [Paragraph(s2, style)]
        story_inframe222 = KeepInFrame(390, 60, story222)
        frame12.addFromList([story_inframe222], c)
        frame1 = Frame(75,count,505,100)
        s = str(i.pregunta)
        story = [Paragraph(s, style)]
        story_inframe = KeepInFrame(380, 60, story)
        frame1.addFromList([story_inframe], c)
        #c.drawString(65,count+90,str(r))


        r=r+1
        if i.respuesta !=None:
            frame4 = Frame(60,count-35,505,100)
            ss2 = str(i.respuesta)
            story11 = [Paragraph(ss2, style)]
            story_inframe21 = KeepInFrame(380, 60, story11)
            frame4.addFromList([story_inframe21], c)
            frame2 = Frame(100,count-35,505,100)
            ss = str(i.comentario)
            story1 = [Paragraph(ss, style)]
            story_inframe2 = KeepInFrame(360, 60, story1)
            frame2.addFromList([story_inframe2], c)
            frame44 = Frame(100,count-100,505,100)
            ss4 = str(i.comentario2)
            story14 = [Paragraph(ss4, style)]
            story_inframe24 = KeepInFrame(360, 60, story14)
            frame44.addFromList([story_inframe24], c)
            #re=Asociada.objects.get(id=i.respuesta_id)
            #c.drawString(100,count+90, str(i.respuesta))
            #c.drawString(160,count+70,str(i.comentario))
            rr=i.seguimiento
            if rr==True:
                 c.drawImage("imagenes/19754.jpg",520,count+55,20,20)

        #if i.pregunta==preg.pregunta:
        else :
            frame3 = Frame(100,count-35,505,100)
            sss = "----------"
            story2 = [Paragraph(sss, style)]
            story_inframe3 = KeepInFrame(380, 60, story2)
            frame3.addFromList([story_inframe3], c)
            frame31 = Frame(60,count-35,505,100)
            sss1 = "---"
            story211 = [Paragraph(sss1, style)]
            story_inframe31 = KeepInFrame(380, 60, story211)
            frame31.addFromList([story_inframe31], c)
            frame34 = Frame(100,count-100,505,100)
            sss4 = "----------"
            story244 = [Paragraph(sss4, style)]
            story_inframe344 = KeepInFrame(380, 60, story244)
            frame34.addFromList([story_inframe344], c)
            rr=i.seguimiento
            if rr==True:
                 c.drawImage("imagenes/19754.jpg",520,count+55,20,20)

        #preg.textLine(str(i.pregunta))
        c.rect(60,count-60,505,160)
        c.line(490,count+100,490,count-60)
        count=count-160
        tt =tt + 1

        #preg.textLine("\n")
        if w==1:
            if tt>2:
                tt=0
                c.showPage()
                c.drawImage("imagenes/Arauco-logo.jpg",60,740,100,100,preserveAspectRatio=True)
                c.setFont("Helvetica",7)
                count=640
                w=w+1
        else:
            if tt>3:
                tt=0
                c.showPage()
                c.drawImage("imagenes/Arauco-logo.jpg",60,740,100,100,preserveAspectRatio=True)
                c.setFont("Helvetica",7)
                count=640
                w=w+1
            '''



    styles = getSampleStyleSheet()
    s = str(nombre)  * 1000
    story = [Paragraph(s, styles['Normal'])]
    story_inframe = KeepInFrame(4*inch, 8*inch, story)
    frame1.addFromList([story_inframe], c)
'''
    c.showPage()
    c.save()
    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


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
    nom.append("cuatrouno")
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
        cate[preguntas[i]].append(preguntas[i].unodiecisiete)
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
        cate[preguntas[i]].append(preguntas[i].cuatrouno)
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
    nom.append("cuatrouno")
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
        comun[comunas[i]].append(comunas[i].unodiecisiete)
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
        comun[comunas[i]].append(comunas[i].cuatrouno)
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


class Pregg(admin.TabularInline):
    model = Pregs
    extra=0
    readonly_fields=('pregunta',)
    can_delete=False


class Prep(admin.ModelAdmin):
    readonly_fields=('pregunta',)
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
        pregunta1 = Realiza.objects.filter(comuna=self.instance.comuna)
        comuna=self.instance.comuna
        print("Comuna1: ",comuna)
        if self.instance.id:
            if len(Pregs.objects.filter(formulario_id_id=self.instance.id))==0:
                print ("entre en el if")
                for i in pregunta1:
                    add=Pregs.objects.create(formulario_id_id=self.instance.id, pregunta=i.pregunta)
                    add.save()
class FormularioAd(admin.ModelAdmin):
    form = ForForm
    inlines =[Pregg,]
    list_filter=('estado_formulario','encargado')
    list_display=('id','rol','comuna','predio','proveedor','encargado','eval_inicial','eval_final','estado_formulario')


    fieldsets=[
       ('INFORMACIÓN PERSONAL', {'fields':[('encargado','proveedor'),('comuna','rol'),'predio']}),
        ('EVIDENCIA DEL LUGAR', {'fields': [('imagen')]}),
        ('ESTADO DE FORMULARIO', {'fields': ['eval_final','estado_formulario']}),
    #{'fields':('preguntas')},
    ]
    actions= [Generar_Formulario]
    search_fields=('id','predio','rol__rol','proveedor__nombre',)


class Comu(admin.ModelAdmin):
      search_fields=('comuna',)
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
'cuatrouno',
'cinco')

class Predios(admin.ModelAdmin):
    list_display=('rol','proveedor')
    search_fields=('rol','proveedor',)
class Pre(admin.ModelAdmin):
  search_fields=('pregunta',)
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
'cuatrouno',
'cinco')
class Provee(admin.ModelAdmin):
    list_display=('nombre','rut')
    search_fields=('nombre','rut',)
  #inlines=[ChoiceInline]


admin.site.register(Comuna,Comu)
admin.site.register(Pregunta,Pre)
admin.site.register(Realiza,REa)
admin.site.register(Proveedor,Provee)
admin.site.register(Rol,Predios)
#admin.site.register(Respuesta)
admin.site.register(Formulario, FormularioAd)
