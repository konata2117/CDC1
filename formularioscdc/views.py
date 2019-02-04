# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import View
from django.db import models
from .models import Realiza
from .models import Proveedor

def cargar_preguntas(request):
    comuna_id=request.GET.get('ANGOL')
    preguntas=Realiza.objects.filter(comuna=comuna_id)

    #return render(request)
        #response = HttpResponse(content_type='application/pdf')
        #buffer=BytesIO()
        #pdf=canvas.Canvas(buffer)
        #pdf.showPage()
        #pdf.save()
        #pdf=buffer.getvalue()
        #buffer.close()
        #response.write(pdf)
        #return response
  
