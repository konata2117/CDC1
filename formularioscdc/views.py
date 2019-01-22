# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import View
from django.db import models
from .utils import render_to_pdf
from .models import Proveedor


def GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(id=kwargs.get('id'))
        context ={
            "proveedor_nombre": proveedor_nombre,
            "proveedor_rut": proveedor_rut
        }
        pdf = render_to_pdf('pdf/pdfs.html',context)
        return HttpResponse(pdf,content_type='application/pdf')
        #response = HttpResponse(content_type='application/pdf')
        #buffer=BytesIO()
        #pdf=canvas.Canvas(buffer)
        #pdf.showPage()
        #pdf.save()
        #pdf=buffer.getvalue()
        #buffer.close()
        #response.write(pdf)
        #return response
  
