from django.shortcuts import render, redirect
from E_Order.forms import OrderForm
from E_Cart.models import Cart, CartItem
from E_Order.models import OrderItem
from E_App.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
login_required(login_url='E_User:Login')
def Order_details(request):
    total_price = 0
    counter = 0
    cart = Cart.objects.get(user = request.user.id)
    cart_items = CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
        total_price += cart_item.product.price * cart_item.quantity
        counter += cart_item.quantity
    form = OrderForm()

    
    return render(request, 'order.html', {'form':form, 'cart_items':cart_items, 'total_price': total_price, 'counter': counter} )

login_required(login_url='E_User:Login')
def Confirm_order(request):
      
    if request.method == 'POST':  

        cart = Cart.objects.get(user = request.user)
        cart_items = CartItem.objects.all().filter(cart=cart)
        total_product_price = 0
     
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            for cart_item in cart_items:
                total_product_price += cart_item.product.price * cart_item.quantity
            order.total_amount = total_product_price
            order.save()

            for cart_item in cart_items:
                order_item = OrderItem.objects.create(
                    products = cart_item.product,
                    quantity = cart_item.quantity,
                    total_price = cart_item.product.price * cart_item.quantity,
                    seller = cart_item.product.seller,
                    order = order
                )
                order_item.save()
                Product.objects.filter(id=cart_item.product.id).update(stock = cart_item.product.stock - cart_item.quantity)

            CartItem.objects.filter(cart=cart).delete()

            return redirect('E_App:AllProdCat')
        else:
            print(form.errors, form.non_field_errors)

    return redirect('E_Order:order')
