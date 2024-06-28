from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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

    path('admin/', views.administrar_inventario, name='administrar_inventario'),
    path('admin/producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('admin/producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('admin/producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),

    path('admin-view/', views.admin_view, name='admin_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('checkout/', views.checkout, name='checkout'),
]
