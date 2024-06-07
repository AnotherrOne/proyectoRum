from django.shortcuts import render
from .models import Tier, Usuario

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
    context ={}
    return render(request, "pages/login.html",context)
def registro(request):
    context={}
    return render(request, "pages/registro.html",context)