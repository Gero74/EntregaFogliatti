from django.urls import path
from AppFogliatti import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
    path('usuario/', views.usuario, name='usuario'),
    path('tematicaApi/', views.tematicaapi),
    path('contactoApi/', views.contactoapi),
    path('busqueda/', views.buscartematica),
    path('buscar/', views.buscar),
    
    
]
