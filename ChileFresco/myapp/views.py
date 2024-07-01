from django.shortcuts import render, redirect
from .models import (
    VerdurasYFrutas,
    Refrigerados,
    Limpieza,
    Carnes,
    Despensa,
    BebidasYLicores,
    QuesoYFiambres,
    PanaderiaYPasteleria,
    Congelados,
    Mascotas,
    BebesYNiños,
    Ferreteria,
)
from .forms import ProductoForm

from .models import VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa, BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados, Mascotas, BebesYNiños, Ferreteria
from django.shortcuts import render, redirect
from .forms import ProductoForm




from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa, BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados, Mascotas, BebesYNiños, Ferreteria

def administrador_agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                categoria = form.cleaned_data['categoria']
                producto = form.save(commit=False)

                # Asignar la instancia del modelo de producto correspondiente según la categoría
                model_map = {
                    'verduras_y_frutas': VerdurasYFrutas,
                    'refrigerados': Refrigerados,
                    'limpieza': Limpieza,
                    'carnes': Carnes,
                    'despensa': Despensa,
                    'bebidas_y_licores': BebidasYLicores,
                    'queso_y_fiambres': QuesoYFiambres,
                    'panaderia_y_pasteleria': PanaderiaYPasteleria,
                    'congelados': Congelados,
                    'mascotas': Mascotas,
                    'bebes_y_ninos': BebesYNiños,
                    'ferreteria': Ferreteria,
                }

                if categoria in model_map:
                    producto_instance = model_map[categoria]()
                    for field in producto._meta.fields:
                        setattr(producto_instance, field.name, getattr(producto, field.name))
                    producto_instance.save()

                    return redirect('administrador')
                else:
                    return render(request, 'crud/ADMINISTRADOR.html', {'form': form, 'error_message': 'Categoría de producto no válida'})

            except Exception as e:
                error_message = f"Error al guardar el producto: {str(e)}"
                return render(request, 'crud/ADMINISTRADOR.html', {'form': form, 'error_message': error_message})

    else:
        form = ProductoForm()

    return render(request, 'crud/ADMINISTRADOR.html', {'form': form})


def administrador(request):
    productos = {
        'verduras_y_frutas': VerdurasYFrutas.objects.all(),
        'refrigerados': Refrigerados.objects.all(),
        'limpieza': Limpieza.objects.all(),
        'carnes': Carnes.objects.all(),
        'despensa': Despensa.objects.all(),
        'bebidas_y_licores': BebidasYLicores.objects.all(),
        'queso_y_fiambres': QuesoYFiambres.objects.all(),
        'panaderia_y_pasteleria': PanaderiaYPasteleria.objects.all(),
        'congelados': Congelados.objects.all(),
        'mascotas': Mascotas.objects.all(),
        'bebes_y_niños': BebesYNiños.objects.all(),
        'ferreteria': Ferreteria.objects.all(),
    }
    return render(request, 'crud/ADMINISTRADOR.html', {'productos': productos})


def productos_view(request):
    productos_por_categoria = {
        'verduras_y_frutas': VerdurasYFrutas.objects.all(),
        'refrigerados': Refrigerados.objects.all(),
        'limpieza': Limpieza.objects.all(),
        'carnes': Carnes.objects.all(),
        'despensa': Despensa.objects.all(),
        'bebidas_y_licores': BebidasYLicores.objects.all(),
        'queso_y_fiambres': QuesoYFiambres.objects.all(),
        'panaderia_y_pasteleria': PanaderiaYPasteleria.objects.all(),
        'congelados': Congelados.objects.all(),
        'mascotas': Mascotas.objects.all(),
        'bebes_y_ninos': BebesYNiños.objects.all(),
        'ferreteria': Ferreteria.objects.all(),
    }
    
    context = {
        'productos_por_categoria': productos_por_categoria
    }
    
    return render(request, 'myapp/PRODUCTOS.html', context)












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
