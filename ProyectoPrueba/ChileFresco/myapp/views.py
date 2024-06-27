from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def productos(request):
    return render(request, 'myapp/PRODUCTOS.html')

def contactanos(request):
    return render(request, 'myapp/CONTACTANOS.html')

