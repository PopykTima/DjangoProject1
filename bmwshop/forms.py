from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'email', 'address', 'comment']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ПІБ'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефону'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Адреса доставки', 'rows': 3}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Коментар (необов’язково)', 'rows': 3}),
        }
