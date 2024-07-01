
from django.contrib import admin
from django.urls import include, path
from myapp import views
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('bebes/', views.bebes, name='bebes'),
    path('carro_compra/', views.carro_compra, name='carro_compra'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('pago/', views.pago, name='pago'),
    path('panaderia/', views.panaderia, name='panaderia'),
    path('terminos_condiciones/', views.terminos_condiciones, name='terminos_condiciones'),
    path('verduleria/', views.verduleria, name='verduleria'),
    path('productos-todos/', productos_view, name='productos_todos'),
    path('administrador/',views.administrador, name='administrador'),
    path('administrador/', views.administrador_agregar_producto, name='administrador_agregar_producto'),
    
    
]
