from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from .models import VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa, BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados, Mascotas, BebesYNiños, Ferreteria
# Create your views here

def productos_view(request):
    verduras_y_frutas = VerdurasYFrutas.objects.all()
    refrigerados = Refrigerados.objects.all()
    limpieza = Limpieza.objects.all()
    carnes = Carnes.objects.all()
    despensa = Despensa.objects.all()
    bebidas_y_licores = BebidasYLicores.objects.all()
    queso_y_fiambres = QuesoYFiambres.objects.all()
    panaderia_y_pasteleria = PanaderiaYPasteleria.objects.all()
    congelados = Congelados.objects.all()
    mascotas = Mascotas.objects.all()
    bebes_y_ninos = BebesYNiños.objects.all()
    ferreteria = Ferreteria.objects.all()
    
    context = {
        'verduras_y_frutas': verduras_y_frutas,
        'refrigerados': refrigerados,
        'limpieza': limpieza,
        'carnes': carnes,
        'despensa': despensa,
        'bebidas_y_licores': bebidas_y_licores,
        'queso_y_fiambres': queso_y_fiambres,
        'panaderia_y_pasteleria': panaderia_y_pasteleria,
        'congelados': congelados,
        'mascotas': mascotas,
        'bebes_y_ninos': bebes_y_ninos,
        'ferreteria': ferreteria,
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

def cart(request):
    contexto = {}
    return render(request, 'myapp/cart.html', contexto)

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

def administrar_inventario(request):
    productos = Producto.objects.all()
    return render(request, 'admin_inventory.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrar_inventario')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administrar_inventario')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('administrar_inventario')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'myapp/admin_view.html')

@login_required
def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        # Lógica para procesar el pedido
        return redirect('index')
    return render(request, 'checkout.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # redirigir a otra página o mostrar un mensaje de éxito
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})