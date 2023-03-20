from django.forms import ModelForm
from django import forms
from E_Order.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = (
            'name',
            'email',
            'phone',
            'city',
            'shipping_address',
            
        )
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control form-control-sm',}),
            'email': forms.EmailInput(attrs= {'class': 'form-control form-control-sm'}),
            'phone': forms.NumberInput(attrs= {'type':'tel', 'class': 'form-control form-control-sm'}),
            'shipping_address': forms.Textarea(attrs= {'class': 'form-control form-control-sm'}),
            'city': forms.TextInput(attrs= {'class': 'form-control form-control-sm'})
        }
