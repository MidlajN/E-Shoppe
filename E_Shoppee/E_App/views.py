from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def AllProdCat(request, cat_slug = None):
    cat_page = None
    product_list = None

    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        product_list = Product.objects.all().filter(category=cat_page, available=True)

    else:
        product_list = Product.objects.all().filter(available=True)

    paginator = Paginator(product_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': cat_page, 'products': products})