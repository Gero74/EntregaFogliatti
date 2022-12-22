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
    print(request.GET)
    codigo_views= request.GET["codigo"]
    tematicas_todas = Tematica.objects.filter(codigo=codigo_views)
    return render(request,"AppFogliatti/resultadotematica.html",{"codigo":codigo_views,"tematica":tematicas_todas})

def buscarcontacto(request):
    return render(request,"AppFogliatti/busquedacontacto.html")

def buscar2(request):
    print(request.GET)
    nombre_views= request.GET["nombre"]
    contacto_todos = Contacto.objects.filter(nombre=nombre_views)
    return render(request,"AppFogliatti/resultadocontacto.html",{"nombre":nombre_views,"contacto":contacto_todos})

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
            return render(request, "AppFogliatti/inicio.html")
    
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
            return render(request, "AppFogliatti/inicio.html")
    
    else:
        miFormulario3 = UsuarioFormulario()

    return render(request,"AppFogliatti/usuario.html", {"miFormulario3": miFormulario3})


def tematicaapi(request):
    tematica_todos = Tematica.objects.all()
    return HttpResponse(serializers.serialize("json",tematica_todos))

def contactoapi(request):
    contacto_todos = Contacto.objects.all()
    return HttpResponse(serializers.serialize("json",contacto_todos))


def leer_tematica(request):
    tematica_all = Tematica.objects.all()
    return HttpResponse(serializers.serialize("json",tematica_all))

def crear_tematica(request):
    tematica = Tematica(nombre_tema="TematicaTest",autor ="Gero",codigo=123)
    tematica.save()
    return HttpResponse(f"Tematica {tematica.nombre_tema} ha sido creado")

def editar_tematica(request):
    nombre_consulta="TematicaTest"
    Tematica.objects.filter(nombre_tema=nombre_consulta).update(nombre_tema="nombrenuevoTematicaTest")
    return HttpResponse(f"Tematica {nombre_consulta} ha sido editado")


def eliminar_tematica(request):
    nombre_nuevo="nombrenuevoTematicaTest"
    tematica=Tematica.objects.filter(nombre_tema=nombre_nuevo)
    tematica.delete()            
    return HttpResponse(f"Tematica {nombre_nuevo} ha sido eliminado")

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView 

class Tematicalist(ListView):
    model = Tematica
    template = "AppFogliatti/tematica_list.html"

class TematicaCreate(CreateView):
    model = Tematica
    fields = "__all__"
    success_url = "/AppFogliatti/tematica/list/"

class TematicaEdit(UpdateView):
    model = Tematica
    fields = "__all__"
    success_url = "/AppFogliatti/tematica/list/"
    
from django.views.generic import DetailView

class TematicaDetail(DetailView):
    model = Tematica
    template_name = "AppFogliatti/tematica_detail.html"

class TematicaDelete(DeleteView):
    model = Tematica
    #fields = "__all__"
    success_url = "/AppFogliatti/tematica/list/"


class Contactolist(ListView):
    model = Contacto
    template = "AppFogliatti/contacto_list.html"

class ContactoCreate(CreateView):
    model = Contacto
    fields = "__all__"
    success_url = "/AppFogliatti/contacto/list/"

class ContactoEdit(UpdateView):
    model = Contacto
    fields = "__all__"
    success_url = "/AppFogliatti/contacto/list/"

class ContactoDetail(DetailView):
    model = Contacto
    template_name = "AppFogliatti/contacto_detail.html"

class ContactoDelete(DeleteView):
    model = Contacto
    #fields = "__all__"
    success_url = "/AppFogliatti/contacto/list/"
    

class Usuariolist(ListView):
    model = Usuario
    template = "AppFogliatti/Usuario_list.html"

class UsuarioCreate(CreateView):
    model = Usuario
    fields = "__all__"
    success_url = "/AppFogliatti/usuario/list/"

class UsuarioEdit(UpdateView):
    model = Usuario
    fields = "__all__"
    success_url = "/AppFogliatti/usuario/list/"

class UsuarioDetail(DetailView):
    model = Usuario
    template_name = "AppFogliatti/usuario_detail.html"

class UsuarioDelete(DeleteView):
    model = Usuario
    #fields = "__all__"
    success_url = "/AppFogliatti/usuario/list/"
    