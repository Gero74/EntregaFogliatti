from django.http import HttpResponse
from django.template import Template, Context
import os.path

from django.template import loader

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATES_PATH = os.path.join(PROJECT_PATH, "templates/")

def saludo(request):
    return HttpResponse("Hola Django Coder")

def probandoTemplate(self):
   
    miHtml = open(TEMPLATES_PATH+"/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)