from django.urls import path
from AppFogliatti import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tematica/', views.blog, name='tematica'),
    path('contacto/', views.contacto, name='contacto'),
    path('usuario/', views.usuario, name='usuario'),
    path('tematicaApi/', views.tematicaapi),
    path('contactoApi/', views.contactoapi),
    path('busquedatematica/', views.buscartematica),
    path('buscar/', views.buscar),
    path('busquedacontacto/', views.buscarcontacto),
    path('buscar2/', views.buscar2),
    path('busquedausuario/', views.buscarusuario),
    path('buscar3/', views.buscar3),
    path('leerTematica/', views.leer_tematica),
    path('crearTematica/', views.crear_tematica),
    path('editarTematica/', views.editar_tematica),
    path('eliminarTematica/', views.eliminar_tematica),
    path('tematica/list/', views.Tematicalist.as_view(),name='List'),
    path('tematica/create/', views.TematicaCreate.as_view(),name='New'),
    path('tematica/edit/<pk>', views.TematicaEdit.as_view(),name='Edit'),
    path('tematica/detail/<pk>', views.TematicaDetail.as_view(),name='Detail'),
    path('tematica/delete/<pk>', views.TematicaDelete.as_view(),name='Delete'),


    path('contacto/list/', views.Contactolist.as_view(),name='ListContacto'),
    path('contacto/create/', views.ContactoCreate.as_view(),name='NewContacto'),
    path('contacto/edit/<pk>', views.ContactoEdit.as_view(),name='EditContacto'),
    path('contacto/detail/<pk>', views.ContactoDetail.as_view(),name='DetailContacto'),
    path('contacto/delete/<pk>', views.ContactoDelete.as_view(),name='DeleteContacto'),

    path('usuario/list/', views.Usuariolist.as_view(),name='ListUsuario'),
    path('usuario/create/', views.UsuarioCreate.as_view(),name='NewUsuario'),
    path('usuario/edit/<pk>', views.UsuarioEdit.as_view(),name='EditUsuario'),
    path('usuario/detail/<pk>', views.UsuarioDetail.as_view(),name='DetailUsuario'),
    path('usuario/delete/<pk>', views.UsuarioDelete.as_view(),name='DeleteUsuario')

   
    
    
]
