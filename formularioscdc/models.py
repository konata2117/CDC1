from django.db import models
from django.utils import timezone

class Proveedor(models.Model):
    nombre=models.CharField(max_length=30)
    rut=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"
class Comuna(models.Model):
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
    cuatro= models.BooleanField(default=True)
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
    cuatro= models.BooleanField(default=True)
    cinco= models.BooleanField(default=True)
    serealiza=models.BooleanField(default=True)
    tipo=models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.pregunta
    class Meta:
        verbose_name="Pregunta"
        verbose_name_plural="Preguntas"

class Realiza(models.Model):
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE)
    pregunta =models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    def __str__(self):
        return self.pregunta

class Respuesta(models.Model):
    #pregunta=models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    respuesta=models.CharField(max_length=30)
    def __str__(self):
        return self.respuesta
    class Meta:
        verbose_name="Respuesta"
        verbose_name_plural="Respuestas"
class Rol(models.Model):
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    rol=models.CharField(max_length=70)
    class Meta:
        verbose_name="Rol"
        verbose_name_plural="Roles"
    def __str__(self):
        return self.rol

    
class Formulario(models.Model):
    encargado=models.ForeignKey( 'auth.User', on_delete=models.CASCADE)
    proveedor =models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE, blank=True,null=True)
    predio=models.CharField(max_length=20)
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='imagenes/', null=True,blank=True) 
    #categoria=models.ForeignKey(Comuna,on_delete=models.CASCADE,blank=True,null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    pregunta=models.ForeignKey(Pregunta,on_delete=models.CASCADE,null=True,blank=True)
    respuesta=models.ForeignKey(Respuesta,on_delete=models.CASCADE,null=True,blank=True)
    def contador_preguntas(self, comuna):
        print ("ACA")
    
    class Meta:
        verbose_name="Formulario"
        verbose_name_plural="Formularios"

