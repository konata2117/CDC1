# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import View
from django.db import models
from .models import Realiza
from .models import Proveedor,Formulario
from django.shortcuts import render

def preguntas(request):
        pregunta=Realiza.objects.filter(comuna="CHIGUAYANTE").order_by('id')
        contexto={'preguntas':pregunta}
        return render(request,'admin/prueba.html',contexto)