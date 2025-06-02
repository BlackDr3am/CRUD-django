from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'imagen']  # Agregamos imagen

    imagen = forms.ImageField(required=False)  # Opcional
