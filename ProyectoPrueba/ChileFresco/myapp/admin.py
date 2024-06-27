from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa, \
    BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados, \
    Mascotas, BebesYNiños, Ferreteria

class ProductoBaseAdmin(admin.ModelAdmin):
    list_display = ('codigo_barra', 'nombre_producto', 'precio_producto', 'peso_volumen_producto', 'unidades_stock', 'unidades_detalle', 'fecha_elaboracion', 'fecha_vencimiento', 'imagen_producto_preview')
    search_fields = ('nombre_producto', 'codigo_barra')
    list_filter = ('fecha_vencimiento',)

    def precio_producto(self, obj):
        return f"${obj.precio_producto:.2f} CLP"
    precio_producto.short_description = 'Precio Producto (CLP)'

    def peso_volumen_producto(self, obj):
        if obj.tipo_unidad == 'peso':
            if obj.peso_volumen_producto >= 1000:
                return f"{obj.peso_volumen_producto / 1000:.2f} kg"
            else:
                return f"{obj.peso_volumen_producto:.2f} g"
        elif obj.tipo_unidad == 'volumen':
            if obj.peso_volumen_producto >= 1000:
                return f"{obj.peso_volumen_producto / 1000:.2f} L"
            else:
                return f"{obj.peso_volumen_producto:.2f} ml"
        elif obj.tipo_unidad == 'unidades':
            return obj.unidades_detalle if obj.unidades_detalle else '-'

    def imagen_producto_preview(self, obj):
        if obj.imagen_producto:
            return mark_safe(f'<img src="{obj.imagen_producto.url}" height="50">')
        else:
            return '-'
    imagen_producto_preview.short_description = 'Imagen'

# Registrar los modelos usando la clase base
@admin.register(VerdurasYFrutas)
class VerdurasYFrutasAdmin(ProductoBaseAdmin):
    pass

@admin.register(Refrigerados)
class RefrigeradosAdmin(ProductoBaseAdmin):
    pass

@admin.register(Limpieza)
class LimpiezaAdmin(ProductoBaseAdmin):
    pass

@admin.register(Carnes)
class CarnesAdmin(ProductoBaseAdmin):
    pass

@admin.register(Despensa)
class DespensaAdmin(ProductoBaseAdmin):
    pass

@admin.register(BebidasYLicores)
class BebidasYLicoresAdmin(ProductoBaseAdmin):
    pass

@admin.register(QuesoYFiambres)
class QuesoYFiambresAdmin(ProductoBaseAdmin):
    pass

@admin.register(PanaderiaYPasteleria)
class PanaderiaYPasteleriaAdmin(ProductoBaseAdmin):
    pass

@admin.register(Congelados)
class CongeladosAdmin(ProductoBaseAdmin):
    pass

@admin.register(Mascotas)
class MascotasAdmin(ProductoBaseAdmin):
    pass

@admin.register(BebesYNiños)
class BebesYNiñosAdmin(ProductoBaseAdmin):
    pass

@admin.register(Ferreteria)
class FerreteriaAdmin(ProductoBaseAdmin):
    pass
