from django.forms import ModelForm
from E_App.models import Product

class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description', 
            'price', 
            'category', 
            'product_image',
            'stock',
            'available',      
        ]