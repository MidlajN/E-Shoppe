from django.shortcuts import render, redirect
from E_App.models import Product
from django.contrib.auth.decorators import login_required
from E_Cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required(login_url='E_User:Login')
def add_cart(request, prod_id):
    product = Product.objects.get(id=prod_id)
    if request.user.is_authenticated:
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)
            cart.save()

        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1

            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart
            )
            cart_item.save()
        return redirect('E_Cart:cart_details')


@login_required(login_url='E_User:Login')
def cart_details(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))
