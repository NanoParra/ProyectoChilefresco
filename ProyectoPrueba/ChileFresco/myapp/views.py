from django.shortcuts import render

# Create your views here

def index(request):
    return render(request, 'myapp/index.html')
    
def bebes(request):
    return render(request, 'productos/BEBECOMESTIBLES.html')

def carro_compra(request):
    return render(request, 'productos/CARRO_COMPRA.html')

def contactanos(request):
    return render(request, 'productos/CONTACTANOS.html')

def cuenta(request):
    return render(request, 'productos/CUENTA.html')

def index(request):
    return render(request, 'productos/index.html')

def pago(request):
    return render(request, 'productos/PAGO.html')

def panaderia(request):
    return render(request, 'productos/PANADERIA.html')

def productos(request):
    return render(request, 'productos/PRODUCTOS.html')

def terminos_condiciones(request):
    return render(request, 'productos/TERMINOS_CONDICIONES.html')

def verduleria(request):
    return render(request, 'productos/VERDULERIA.html')