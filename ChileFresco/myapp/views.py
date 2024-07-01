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
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductoForm
from .models import ProductoBase
from django.http import JsonResponse




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
                if categoria == 'verduras_y_frutas':
                    producto_instance = VerdurasYFrutas()
                elif categoria == 'refrigerados':
                    producto_instance = Refrigerados()
                elif categoria == 'limpieza':
                    producto_instance = Limpieza()
                elif categoria == 'carnes':
                    producto_instance = Carnes()
                elif categoria == 'despensa':
                    producto_instance = Despensa()
                elif categoria == 'bebidas_y_licores':
                    producto_instance = BebidasYLicores()
                elif categoria == 'queso_y_fiambres':
                    producto_instance = QuesoYFiambres()
                elif categoria == 'panaderia_y_pasteleria':
                    producto_instance = PanaderiaYPasteleria()
                elif categoria == 'congelados':
                    producto_instance = Congelados()
                elif categoria == 'mascotas':
                    producto_instance = Mascotas()
                elif categoria == 'bebes_y_ninos':
                    producto_instance = BebesYNiños()
                elif categoria == 'ferreteria':
                    producto_instance = Ferreteria()
                else:
                    return render(request, 'crud/ADMINISTRADOR.html', {'form': form, 'error_message': 'Categoría de producto no válida'})

                # Llenar los campos del modelo específico con los datos del formulario y guardar
                producto_instance.nombre_producto = producto.nombre_producto
                producto_instance.precio_producto = producto.precio_producto
                producto_instance.peso_volumen_producto = producto.peso_volumen_producto
                producto_instance.tipo_unidad = producto.tipo_unidad
                producto_instance.unidades_stock = producto.unidades_stock
                producto_instance.unidades_detalle = producto.unidades_detalle
                producto_instance.fecha_elaboracion = producto.fecha_elaboracion
                producto_instance.fecha_vencimiento = producto.fecha_vencimiento
                producto_instance.imagen_producto = producto.imagen_producto
                producto_instance.save()

                # Redirigir a la página de administrador con éxito
                return redirect('administrador')

            except Exception as e:
                # Manejo genérico de errores durante el proceso de guardar el producto
                error_message = f"Error al guardar el producto: {str(e)}"
                return render(request, 'crud/ADMINISTRADOR.html', {'form': form, 'error_message': error_message})

    else:
        form = ProductoForm()

    contexto = {'form': form}
    return render(request, 'crud/ADMINSTRADOR.html', contexto)

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

def modificar_producto(request, pk):
    producto = get_object_or_404(ProductoForm, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administrador')  # Redirige a la página de administrador o donde corresponda
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'crud/ADMINISTRADOR.html', {'productos': productos})









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
