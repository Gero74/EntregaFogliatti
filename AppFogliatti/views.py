from django.shortcuts import render
from django.http import HttpResponse

from AppFogliatti.models import Usuario
from AppFogliatti.models import Contacto
from AppFogliatti.models import Tematica
from django.core import serializers
from AppFogliatti.forms import TematicaFormulario
from AppFogliatti.forms import ContactoFormulario
from AppFogliatti.forms import UsuarioFormulario

# Create your views here.
def buscar(request):
    nombre= request.GET ["nombre"]
    return HttpResponse(f"Estoy buscando el nombre: {nombre}")

def buscartematica(request):
    return render(request,"AppFogliatti/busqueda.html")


def inicio(request):
    return render(request,"AppFogliatti/inicio.html")

def contacto(request):
    if request.method == "POST":

        miFormulario2 = ContactoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario2)
        
        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data
            tematica = Contacto(nombre=informacion["nombre"], correo=informacion["correo"], descripcion=informacion["descripcion"])
            tematica.save()
            return render(request, "AppFogliatti/contacto.html")
    
    else:
        miFormulario2 = ContactoFormulario()

    return render(request,"AppFogliatti/contacto.html", {"miFormulario2": miFormulario2})


def blog(request):
    if request.method == "POST":

        miFormulario = TematicaFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            tematica = Tematica(nombre_tema=informacion["nombre_tema"], autor=informacion["autor"], codigo=informacion["codigo"])
            tematica.save()
            return render(request, "AppFogliatti/inicio.html")
    
    else:
        miFormulario = TematicaFormulario()
    
    return render(request, "AppFogliatti/blog.html", {"miFormulario": miFormulario})

def usuario(request):
    if request.method == "POST":

        miFormulario3 = UsuarioFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario3)
        
        if miFormulario3.is_valid:
            informacion = miFormulario3.cleaned_data
            tematica = Usuario(nombre=informacion["nombre"], correo=informacion["correo"], nacionalidad=informacion["nacionalidad"])
            tematica.save()
            return render(request, "AppFogliatti/usuario.html")
    
    else:
        miFormulario3 = UsuarioFormulario()

    return render(request,"AppFogliatti/usuario.html", {"miFormulario3": miFormulario3})


def tematicaapi(request):
    tematica_todos = Tematica.objects.all()
    return HttpResponse(serializers.serialize("json",tematica_todos))

def contactoapi(request):
    contacto_todos = Contacto.objects.all()
    return HttpResponse(serializers.serialize("json",contacto_todos))
    