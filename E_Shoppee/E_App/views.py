from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.
def AllProdCat(request, cat_slug = None):
    cat_page = None

    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        product_list = Product.objects.all().filter(category=cat_page, available=True)

    else:
        product_list = Product.objects.all().filter(available=True)

    return render(request, 'category.html', {'category': cat_page, 'products': product_list})