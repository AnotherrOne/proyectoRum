from proyectorum.urls import path
from rum import views

urlpatterns = [
    path("",views.index,name='index'),
    path("servicio",views.servicio,name='servicio'),
    path("informacion", views.informacion, name="informacion"),
    path("contacto",views.contacto,name='contacto'),
    path("clientes",views.clientes,name='clientes'),
    path("login",views.login,name='login'),
    path("registro",views.registro,name="registro"),
    path("usuario_add",views.usuario_add,name="usuario_add"),
    path("servicio_add",views.servicio_add,name="servicio_add"),

]