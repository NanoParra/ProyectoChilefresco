from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('productos/verduras/', views.productos_view, {'categoria': 'Verduras y Frutas'}, name='productos_verduras'),
    path('productos/refrigerados/', views.productos_view, {'categoria': 'Refrigerados'}, name='productos_refrigerados'),
    path('productos/limpieza/', views.productos_view, {'categoria': 'Limpieza'}, name='productos_limpieza'),
    path('productos/carnes/', views.productos_view, {'categoria': 'Carnes'}, name='productos_carnes'),
    path('productos/despensa/', views.productos_view, {'categoria': 'Despensa'}, name='productos_despensa'),
    path('productos/bebidas/', views.productos_view, {'categoria': 'Bebidas y Licores'}, name='productos_bebidas'),
    path('productos/quesos/', views.productos_view, {'categoria': 'Queso y Fiambres'}, name='productos_quesos'),
    path('productos/panaderia/', views.productos_view, {'categoria': 'Panadería y Pastelería'}, name='productos_panaderia'),
    path('productos/congelados/', views.productos_view, {'categoria': 'Congelados'}, name='productos_congelados'),
    path('productos/mascotas/', views.productos_view, {'categoria': 'Mascotas'}, name='productos_mascotas'),
    path('productos/bebes/', views.productos_view, {'categoria': 'Bebés y Niños'}, name='productos_bebes'),
    path('productos/ferreteria/', views.productos_view, {'categoria': 'Ferretería'}, name='productos_ferreteria'),


    path('contactanos/', views.contactanos, name='contactanos'),
    path('bebes/', views.bebes, name='bebes'),
    path('cart/', views.cart, name='cart'),
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
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('signup/', views.signup, name='signup'),

    path('checkout/', views.checkout, name='checkout'),
]
