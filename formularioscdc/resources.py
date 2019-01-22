from import_export import resources
from .models import Formulario
from import_export import fields
class FormularioResource(resources.ModelResource):
    class Meta:
        model = Formulario
        fields = ('id', 'rol', 'proveedor','encargado','created_date',)