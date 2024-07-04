from django.shortcuts import render
from .models import Tier, Usuario
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
def index(request):
    context ={}
    return render(request,'pages/index.html',context)
def servicio(request):
    context ={}
    return render(request, "pages/servicio.html",context)
def informacion(request):
    context ={}
    return render(request, "pages/informacion.html",context)
def contacto(request):
    context ={}
    return render(request, "pages/contacto.html",context)
def clientes(request):
    context ={}
    return render(request, "pages/clientes.html",context)
def login(request):
    if request.method=="POST":
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        if email == "benjamin@papumail.com" and pass1 == "pass123":
            request.session["email"] = email
        else:
            context={
                "mensaje":"usuario o contraseña incorrecta"
            }
            return render(request,"pages/login.html",context)
    else:
        context={
        }
        return render(request,"pages/login.html",context)
def registro(request):
    if request.method=="POST":
        nombre = request.POST["nombre"]
        apellido_paterno = request.POST["apellido_paterno"]
        apellido_materno = request.POST["apellido_materno"]
        email = request.POST["email"]
        password = request.POST["password"]
        id_tier = request.POST["id_tier"]
    context={}
    return render(request, "pages/registro.html",context)
def usuario_add(request):
    context={}
    return render(request, "pages/usuario_add.html",context)
def servicio_add(request):
    context={}
    return render(request, "pages/servicio_add.html",context)