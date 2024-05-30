from proyectorum.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("servicio",views.servicio,name='servicio'),
    path("informacion", views.informacion, name="informacion"),
    path("contacto",views.contacto,name='contacto'),
    path("clientes",views.clientes,name='clientes'),
    path("login",views.login,name='login'),
]