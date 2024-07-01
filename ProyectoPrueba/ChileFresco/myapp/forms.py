from django import forms
from .models import ProductoBase

class ProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoBase
        fields = '__all__' 