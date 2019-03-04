from django.db import models
from django.utils import timezone

class Proveedor(models.Model): #Tabla que tiene almacenado los proveedores existentes en la base de datos
    nombre=models.CharField(max_length=200)
    rut=models.CharField(max_length=30)

    def __str__(self):
        return self.rut #retorna el nombre del proveedor
    class Meta:
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"
        ordering = ['rut']

class Comuna(models.Model): #tabla que contiene informacion de las comunas con sus respectivos riegos, la comuna es clave primaria, es decir esta tabla no posee id
    comuna =models.CharField(max_length=30, primary_key=True)
    unouno= models.BooleanField(default=True)
    unodos= models.BooleanField(default=True)
    unotres= models.BooleanField(default=True)
    unocuatro= models.BooleanField(default=True)
    unocinco= models.BooleanField(default=True)
    unoseis= models.BooleanField(default=True)
    unosiete= models.BooleanField(default=True)
    unoocho= models.BooleanField(default=True)
    unonueve= models.BooleanField(default=True)
    unodiez= models.BooleanField(default=True)
    unoonce= models.BooleanField(default=True)
    unodoce= models.BooleanField(default=True)
    unotrece= models.BooleanField(default=True)
    unocatorce= models.BooleanField(default=True)
    unoquince= models.BooleanField(default=True)
    unodieciseis= models.BooleanField(default=True)
    unodiecisiete= models.BooleanField(default=True)
    unodieciocho= models.BooleanField(default=True)
    unodiecinueve= models.BooleanField(default=True)
    unoveinte= models.BooleanField(default=True)
    unoveintiuno= models.BooleanField(default=True)
    dosuno= models.BooleanField(default=True)
    dosdos= models.BooleanField(default=True)
    dostres= models.BooleanField(default=True)
    tres= models.BooleanField(default=True)
    tresuno= models.BooleanField(default=True)
    tresdos= models.BooleanField(default=True)
    trestres= models.BooleanField(default=True)
    trescuatro= models.BooleanField(default=True)
    trescinco= models.BooleanField(default=True)
    tresseis= models.BooleanField(default=True)
    cuatrouno= models.BooleanField(default=True)

    cinco= models.BooleanField(default=True)
    def __str__(self):
        return self.comuna
    class Meta:
        verbose_name="Comuna"
        verbose_name_plural="Comunas"
class Pregunta(models.Model):
    #comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE, null=True, blank=True)
    pregunta=models.CharField(max_length=200)
    unouno= models.BooleanField(default=True)
    unodos= models.BooleanField(default=True)
    unotres= models.BooleanField(default=True)
    unocuatro= models.BooleanField(default=True)
    unocinco= models.BooleanField(default=True)
    unoseis= models.BooleanField(default=True)
    unosiete= models.BooleanField(default=True)
    unoocho= models.BooleanField(default=True)
    unonueve= models.BooleanField(default=True)
    unodiez= models.BooleanField(default=True)
    unoonce= models.BooleanField(default=True)
    unodoce= models.BooleanField(default=True)
    unotrece= models.BooleanField(default=True)
    unocatorce= models.BooleanField(default=True)
    unoquince= models.BooleanField(default=True)
    unodieciseis= models.BooleanField(default=True)
    unodiecisiete= models.BooleanField(default=True)
    unodieciocho= models.BooleanField(default=True)
    unodiecinueve= models.BooleanField(default=True)
    unoveinte= models.BooleanField(default=True)
    unoveintiuno= models.BooleanField(default=True)
    dosuno= models.BooleanField(default=True)
    dosdos= models.BooleanField(default=True)
    dostres= models.BooleanField(default=True)
    tres= models.BooleanField(default=True)
    tresuno= models.BooleanField(default=True)
    tresdos= models.BooleanField(default=True)
    trestres= models.BooleanField(default=True)
    trescuatro= models.BooleanField(default=True)
    trescinco= models.BooleanField(default=True)
    tresseis= models.BooleanField(default=True)
    cuatrouno= models.BooleanField(default=True)

    cinco= models.BooleanField(default=True)
    #serealiza=models.BooleanField(default=True)
    #tipo=models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.pregunta
    class Meta:
        verbose_name="Pregunta"
        verbose_name_plural="Preguntas"

class Realiza(models.Model):
    comuna=models.CharField(max_length=100,blank=True,null=True)
    pregunta =models.CharField(max_length=300,blank=True,null=True)
    def __str__(self):
        return str(self.pregunta)
    class Meta:
        verbose_name="Asociación"
        verbose_name_plural="Asociación comuna-pregunta"

class Rol(models.Model):
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    rol=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        verbose_name="Rol"
        verbose_name_plural="Roles"
    def __str__(self):
        return self.rol



class Formulario(models.Model):
    FINALIZADO='FINALIZADO'
    PROCESO='EN PROCESO'
    cho=(('SI','SI'),('NO','NO'),('N/A','N/A'), ('OTRO','OTRO'),)
    Res=((FINALIZADO,'FINALIZADO'),(PROCESO,'EN PROCESO'),)
    encargado=models.ForeignKey( 'auth.User', on_delete=models.CASCADE)
    proveedor =models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE, blank=True,null=True)
    predio=models.CharField(max_length=200,null=True,blank=True,default="Sin Nombre")
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE,blank=True,null=True)
    imagen=models.ImageField(upload_to='imagenes/', null=True,blank=True)
    #categoria=models.ForeignKey(Comuna,on_delete=models.CASCADE,blank=True,null=True)
    eval_inicial = models.DateTimeField(default=timezone.now)
    #pregunta=models.ForeignKey(Realiza,blank=True,null=True,on_delete=models.CASCADE)
    #respuesta=models.CharField(max_length=400,null=True,blank=True,choices=cho)
    #comentario =models.CharField(max_length=300,blank=True,null=True)
    estado_formulario=models.CharField(max_length=30,choices=Res, null=True,blank=True)
    eval_final = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.predio
    class Meta:
        verbose_name="Formulario"
        verbose_name_plural="Formularios"

class Pregs(models.Model):
    cho=(('SI','SI'),('NO','NO'),('N/A','N/A'), ('OTRO','OTRO'),)


    formulario_id=models.ForeignKey(Formulario,on_delete=models.CASCADE,null=True,blank=True)
    pregunta=models.CharField(max_length=400,null=True,blank=True)
    #respuesta=models.CharField(max_length=400,null=True,blank=True)
    seguimiento=models.BooleanField(default=False)
    respuesta=models.CharField(max_length=400,null=True,blank=True,choices=cho)#aqui esta el filtrado para las respuesta ver y pensar
    comentario =models.CharField(max_length=400,null=True,default="Sin Comentarios")
    comentario2 =models.CharField(max_length=400,null=True,default="Sin Comentarios")
    def __str__(self):
        return str(self.formulario_id)
    class Meta:
        verbose_name="Medidas de Control"
        verbose_name_plural="Medidas de Control"
