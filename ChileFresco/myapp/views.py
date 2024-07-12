from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required #type: ignore
from django.contrib.auth.forms import UserCreationForm
from .models import (
    VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa,
    BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados,
    Mascotas, BebesYNiños, Ferreteria
)
from .forms import (
    VerdurasYFrutasForm, RefrigeradosForm, LimpiezaForm, CarnesForm, DespensaForm,
    BebidasYLicoresForm, QuesoYFiambresForm, PanaderiaYPasteleriaForm, CongeladosForm,
    MascotasForm, BebesYNiñosForm, FerreteriaForm
)

def administrador_modificar_producto(request, product_type, codigo_barra):
    # Determina el modelo y formulario según el tipo de producto
    model_class = {
        'verduras': VerdurasYFrutas,
        'refrigerados':Refrigerados, 
        'limpieza': Limpieza, 
        'carnes':Carnes, 
        'despensa':Despensa, 
        'bebidas':BebidasYLicores, 
        'quesos':QuesoYFiambres, 
        'panaderia':PanaderiaYPasteleria, 
        'congelados':Congelados, 
        'mascotas':Mascotas, 
        'bebes':BebesYNiños, 
        'ferreteria':Ferreteria
        # Agrega los demás modelos según sea necesario
    }.get(product_type)

    form_class = {
        'verduras': VerdurasYFrutasForm,
        'refrigerados': RefrigeradosForm, 
        'limpieza': LimpiezaForm, 
        'carnes': CarnesForm, 
        'despensa': DespensaForm, 
        'bebidas': BebidasYLicoresForm, 
        'quesos': QuesoYFiambresForm, 
        'panaderia': PanaderiaYPasteleriaForm, 
        'congelados': CongeladosForm, 
        'mascotas': MascotasForm, 
        'bebes': BebesYNiñosForm, 
        'ferreteria': FerreteriaForm
        # Agrega los demás forms según sea necesario
    }.get(product_type)

    # Obtiene la instancia del producto a modificar
    producto = get_object_or_404(model_class, codigo_barra=codigo_barra)

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administrador')  # Redirige a la página de administrador o a otra página
    else:
        form = form_class(instance=producto)

    return render(request, 'crud/modificar_producto.html', {'form': form})

def administrador_eliminar_producto(request, product_type, codigo_barra):
    # Determina el modelo según el tipo de producto
    model_class = {
        'verduras': VerdurasYFrutas,
        'refrigerados':Refrigerados, 
        'limpieza': Limpieza, 
        'carnes':Carnes, 
        'despensa':Despensa, 
        'bebidas':BebidasYLicores, 
        'quesos':QuesoYFiambres, 
        'panaderia':PanaderiaYPasteleria, 
        'congelados':Congelados, 
        'mascotas':Mascotas, 
        'bebes':BebesYNiños, 
        'ferreteria':Ferreteria
    }.get(product_type)

    # Obtiene la instancia del producto a eliminar
    producto = get_object_or_404(model_class, codigo_barra=codigo_barra)

    if request.method == 'POST':
        producto.delete()
        return redirect('administrador')  # Redirige a la página de administrador o a otra página

    return render(request, 'crud/eliminar_producto.html', {'producto': producto})

def administrador_agregar_producto(request, product_type):
    form_class = {
        'verduras': VerdurasYFrutasForm,
        'refrigerados': RefrigeradosForm,
        'limpieza': LimpiezaForm,
        'carnes': CarnesForm,
        'despensa': DespensaForm,
        'bebidas': BebidasYLicoresForm,
        'quesos': QuesoYFiambresForm,
        'panaderia': PanaderiaYPasteleriaForm,
        'congelados': CongeladosForm,
        'mascotas': MascotasForm,
        'bebes': BebesYNiñosForm,
        'ferreteria': FerreteriaForm,
    }.get(product_type)

    if not form_class:
        return redirect('administrador')  # Redirect to admin page if product_type is invalid

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('administrador')  # Redirect to admin page after successful form submission
    else:
        form = form_class()

    return render(request, 'crud/agregar_producto.html', {'form': form})





def administrador(request):
    productos = {
        'verduras': VerdurasYFrutas.objects.all(),
        'refrigerados': Refrigerados.objects.all(),
        'limpieza': Limpieza.objects.all(),
        'carnes': Carnes.objects.all(),
        'despensa': Despensa.objects.all(),
        'bebidas': BebidasYLicores.objects.all(),
        'quesos': QuesoYFiambres.objects.all(),
        'panaderia': PanaderiaYPasteleria.objects.all(),
        'congelados': Congelados.objects.all(),
        'mascotas': Mascotas.objects.all(),
        'bebes': BebesYNiños.objects.all(),
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


# ---------------Login-------------
def login (request):
    contexto = {}
    return render(request, 'registration/login.html', contexto)

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
    else:  
        form = UserCreationForm()
    contexto ={ 'form' : form}
    return render(request, 'registration/register.html', contexto)


@login_required
def adminseccion(request):
    request.session["usuario"]="adminparra";
    usuario=request.session["usuario"]
    contexto = {"usuario":usuario}
    return render(request, 'crud/ADMINISTRADOR.html', contexto)

