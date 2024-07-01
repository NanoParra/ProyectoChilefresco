from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone

UNIDAD_CHOICES = [
    ('peso', 'Peso'),
    ('volumen', 'Volumen'),
    ('unidades', 'Unidades'),
]

class ProductoBase(models.Model):
    # Campos existentes
    codigo_barra = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    peso_volumen_producto = models.FloatField(validators=[MinValueValidator(0.1)])  # assuming weight is in kg or volume in ml
    tipo_unidad = models.CharField(max_length=9, choices=UNIDAD_CHOICES, default='peso')
    unidades_stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    unidades_detalle = models.CharField(max_length=50, blank=True, null=True)
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()
    imagen_producto = models.ImageField(upload_to='productos/', blank=True, null=True)  # Campo para la imagen del producto

    def __str__(self):
        return f'{self.nombre_producto} - {self.codigo_barra}'

    def is_expired(self):
        return self.fecha_vencimiento < timezone.now().date()

    class Meta:
        abstract = True
        ordering = ['fecha_vencimiento']




class VerdurasYFrutas(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Verdura y Fruta"
        verbose_name_plural = "Verduras y Frutas"

class Refrigerados(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Refrigerado"
        verbose_name_plural = "Refrigerados"

class Limpieza(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Producto de Limpieza"
        verbose_name_plural = "Productos de Limpieza"

class Carnes(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Carne"
        verbose_name_plural = "Carnes"

class Despensa(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Producto de Despensa"
        verbose_name_plural = "Productos de Despensa"

class BebidasYLicores(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Bebida y Licor"
        verbose_name_plural = "Bebidas y Licores"

class QuesoYFiambres(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Queso y Fiambre"
        verbose_name_plural = "Quesos y Fiambres"

class PanaderiaYPasteleria(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Producto de Panadería y Pastelería"
        verbose_name_plural = "Productos de Panadería y Pastelería"

class Congelados(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Producto Congelado"
        verbose_name_plural = "Productos Congelados"

class Mascotas(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Producto para Mascotas"
        verbose_name_plural = "Productos para Mascotas"

class BebesYNiños(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Producto para Bebés y Niños"
        verbose_name_plural = "Productos para Bebés y Niños"

class Ferreteria(ProductoBase):
    class Meta(ProductoBase.Meta):
        verbose_name = "Producto de Ferretería"
        verbose_name_plural = "Productos de Ferretería"

    
    
    
    