from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from E_App.forms import ProductAddForm
from django.contrib import messages

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


def ProductDetail(request, cat_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=cat_slug, slug=product_slug)

    except Exception as e:
        raise e
    
    return render(request, 'product.html', {'product': product})


def SearchResult(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Product.objects.all().filter(
            Q(name__contains=query) | Q(category__name__contains=query) | Q(description__contains=query)
            )
        number = len(product)

        return render(request, 'search.html', {'query': query, 'products': product, 'number': number})
    

def AddProduct(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ProductAddForm(request.POST, request.FILES)
            
            for field in form:
                print(field.value())

            if form.is_valid():
                obj = form.save(commit=False)
                obj.seller = request.user
                obj.save()
                return redirect('E_User:Dashboard')
            else:
                messages.info(request, 'Invalid')
                print(form.errors)
                print(form.non_field_errors)

    form = ProductAddForm()
    return render(request, 'addproduct.html', {'form': form})