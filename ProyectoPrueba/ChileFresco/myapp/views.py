from django.shortcuts import render

# Create your views here

def index(request):
    contexto = {}
    return render(request, 'myapp/index.html', contexto)

def productos(request):
    contexto = {}
    return render(request, 'myapp/PRODUCTOS.html', contexto)

def contactanos(request):
    contexto = {}
    return render(request, 'myapp/CONTACTANOS.html', contexto)

def bebes(request):
    contexto = {}
    return render(request, 'myapp/BEBECOMESTIBLES.html', contexto)

def carro_compra(request):
    contexto = {}
    return render(request, 'myapp/CARRO_COMPRA.html', contexto)

def cuenta(request):
    contexto = {}
    return render(request, 'myapp/CUENTA.html', contexto)

def pago(request):
    contexto = {}
    return render(request, 'myapp/PAGO.html', contexto)

def panaderia(request):
    contexto = {}
    return render(request, 'myapp/PANADERIA.html', contexto)

def terminos_condiciones(request):
    contexto = {}
    return render(request, 'myapp/TERMINOS_CONDICIONES.html', contexto)

def verduleria(request):
    contexto = {}
    return render(request, 'myapp/VERDULERIA.html', contexto)
