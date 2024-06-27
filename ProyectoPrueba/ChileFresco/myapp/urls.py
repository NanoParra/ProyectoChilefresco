
from django.urls import path
from . import views

urlpatterns = [
    path('bebes/', views.bebes, name='bebes'),
    path('carro_compra/', views.carro_compra, name='carro_compra'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('', views.index, name='index'),
    path('pago/', views.pago, name='pago'),
    path('panaderia/', views.panaderia, name='panaderia'),
    path('productos/', views.productos, name='productos'),
    path('terminos_condiciones/', views.terminos_condiciones, name='terminos_condiciones'),
    path('verduleria/', views.verduleria, name='verduleria'),
]
    

