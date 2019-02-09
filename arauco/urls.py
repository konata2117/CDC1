"""arauco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from formularioscdc.views import preguntas
from django.urls import reverse
import forms_builder.forms.urls
urlpatterns = [
    url(r'^admin/formularioscdc/formulario/2/change',preguntas, name="preguntas"),
    url(r'^admin/',admin.site.urls),
    url(r'^forms/', include(forms_builder.forms.urls)),
    url(r'^chaining/',include('smart_selects.urls')),
    #path('admin/', admin.site.urls),
    #path('pdf/', views.generate_pdf, name='pdf'),

    #url(r'^pdf/
    # $',PDFTemplateView.as_view(template_name='my_template.html',filename='my_pdf.pdf'), name='pdf'),
    #url(r'^$',views.index.name='indec'),
]
