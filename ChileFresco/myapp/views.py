from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from .models import Carrito
from .forms import CarritoForm
from .models import Order
from .forms import CheckoutForm
from .forms import UserEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa, BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados, Mascotas, BebesYNiños, Ferreteria
# Create your views here
def productos_view(request, categoria=None):
    print(f"Categoría recibida: {categoria}")

    categorias = {
        'Verduras y Frutas': VerdurasYFrutas.objects.all(),
        'Refrigerados': Refrigerados.objects.all(),
        'Limpieza': Limpieza.objects.all(),
        'Carnes': Carnes.objects.all(),
        'Despensa': Despensa.objects.all(),
        'Bebidas y Licores': BebidasYLicores.objects.all(),
        'Queso y Fiambres': QuesoYFiambres.objects.all(),
        'Panadería y Pastelería': PanaderiaYPasteleria.objects.all(),
        'Congelados': Congelados.objects.all(),
        'Mascotas': Mascotas.objects.all(),
        'Bebés y Niños': BebesYNiños.objects.all(),
        'Ferretería': Ferreteria.objects.all(),
    }

    if categoria and categoria in categorias:
        productos = categorias[categoria]
        print(f"Productos encontrados para {categoria}: {productos}")
    else:
        productos = Producto.objects.all()
        print("Productos generales: ", productos)

    context = {
        'categorias': categorias.keys(),
        'productos': productos,
        'categoria_actual': categoria,
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
    return render(request, 'myapp/carro_compra.html', contexto)

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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes redirigir a donde quieras después del signup
            return redirect('index')  # Cambia 'index' por la URL a la que quieres redirigir
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def agregar_al_carrito(request, producto_id):
    if request.method == 'POST':
        form = CarritoForm(request.POST)
        if form.is_valid():
            carrito = form.save(commit=False)
            carrito.usuario = request.user
            carrito.save()
            return redirect('carrito')  # Cambia 'carrito' por la URL de tu carrito de compra
    else:
        form = CarritoForm(initial={'producto': producto_id})
    return render(request, 'agregar_al_carrito.html', {'form': form})

def eliminar_del_carrito(request, carrito_id):
    carrito = Carrito.objects.get(id=carrito_id)
    carrito.delete()
    return redirect('carrito')  # Cambia 'carrito' por la URL de tu carrito de compra

# Otras funciones para actualizar cantidades, etc.

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Guardar la orden en la base de datos
            order = form.save(commit=False)
            order.usuario = request.user  # Asigna el usuario actual
            order.save()
            # Aquí podrías agregar lógica adicional, como enviar un correo de confirmación, procesar el pago, etc.
            return redirect('orden_confirmada')  # Cambia 'orden_confirmada' por la URL de confirmación de orden
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Cambia 'perfil' por la URL de perfil de usuario
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión para mantener al usuario logueado
            return redirect('perfil')  # Cambia 'perfil' por la URL de perfil de usuario
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'cambiar_contraseña.html', {'form': form})