
from django.urls import include, path
from . import views
from .views import productos_view
from django.conf import settings
from django.conf.urls.static import static

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
    path('productos-todos/', productos_view, name='productos_todos'),

    path('administrador/',views.administrador, name='administrador'),
    path('administrador/agregar/<str:product_type>/', views.administrador_agregar_producto, name='administrador_agregar_producto'),
    path('modificar-producto/<str:product_type>/<int:codigo_barra>/', views.administrador_modificar_producto, name='administrador_modificar_producto'),
    path('eliminar-producto/<str:product_type>/<int:codigo_barra>/', views.administrador_eliminar_producto, name='administrador_eliminar_producto'),
    
    path('adminseccion/', views.adminseccion, name='adminseccion'),
    path('login/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    


