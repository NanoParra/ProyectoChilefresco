from django import forms
from .models import VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa, BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados, Mascotas, BebesYNiños, Ferreteria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = VerdurasYFrutas  # Utiliza uno de tus modelos como base
        fields = ['categoria', 'codigo_barra', 'nombre_producto', 'precio_producto', 'peso_volumen_producto', 'tipo_unidad', 'unidades_stock', 'unidades_detalle', 'fecha_elaboracion', 'fecha_vencimiento', 'imagen_producto']
