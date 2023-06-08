from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'type': 'Tipo',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control form-control-sm w-100'}),
            'year': forms.TextInput(attrs={'class': 'form-control form-control-sm w-100', 'type': 'number'}),
            'type': forms.Select(attrs={'class': 'form-select form-select-sm w-100'}),
            'price': forms.TextInput(attrs={'class': 'form-control form-control-sm w-100', 'type': 'number'}),
            'model': forms.TextInput(attrs={'class': 'form-control form-control-sm w-100'}),
        }
