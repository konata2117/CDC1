from import_export import resources, fields
from .models import Formulario

class FormularioResource(resources.ModelResource):
    id=fields.Field(column_name='id', attribute="id")
    rol=fields.Field(column_name='rol',attribute="rol")
    proveedor=fields.Field(column_name='proveedor', attribute="proveedor")
    encargado=fields.Field(column_name='encargado',attribute="encargado")
    created_date=fields.Field(column_name='created_date',attribute="created_date")
    class Meta:
        model = Formulario
        fields = ('id', 'rol', 'proveedor','encargado','created_date',)