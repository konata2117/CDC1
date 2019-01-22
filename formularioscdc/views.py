# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Proveedor
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View



def generate_pdf(request):
    proveedor = Proveedor.objects.all()
    for proveedors in proveedor:
        proveedor_nombre=proveedors.nombre 
        proveedor_rut=proveedors.rut
    context ={
            "proveedor": proveedor,
            "proveedor_nombre": proveedor_nombre,
            "proveedor_rut": proveedor_rut
        }
        #response = HttpResponse(content_type='application/pdf')
        #buffer=BytesIO()
        #pdf=canvas.Canvas(buffer)
        #pdf.showPage()
        #pdf.save()
        #pdf=buffer.getvalue()
        #buffer.close()
        #response.write(pdf)
        #return response
    return render(request,'pdfs.html',context)
