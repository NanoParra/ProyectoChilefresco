from django import forms
from .models import (
    VerdurasYFrutas, Refrigerados, Limpieza, Carnes, Despensa,
    BebidasYLicores, QuesoYFiambres, PanaderiaYPasteleria, Congelados,
    Mascotas, BebesYNiños, Ferreteria, UNIDAD_CHOICES
)

class ProductoFormBase(forms.ModelForm):
    class Meta:
        model = None  # Este será definido en cada formulario específico
        fields = '__all__'

class VerdurasYFrutasForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = VerdurasYFrutas

class RefrigeradosForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Refrigerados

class LimpiezaForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Limpieza

class CarnesForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Carnes

class DespensaForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Despensa

class BebidasYLicoresForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = BebidasYLicores

class QuesoYFiambresForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = QuesoYFiambres

class PanaderiaYPasteleriaForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = PanaderiaYPasteleria

class CongeladosForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Congelados

class MascotasForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Mascotas

class BebesYNiñosForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = BebesYNiños

class FerreteriaForm(ProductoFormBase):
    class Meta(ProductoFormBase.Meta):
        model = Ferreteria
