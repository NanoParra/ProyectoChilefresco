
from django.urls import path
from . import views

urlpatterns = [
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
]
    


