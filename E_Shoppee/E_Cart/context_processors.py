from .models import Cart, CartItem


def counter(request):
    item_count = 0
    user = request.user.id
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(user=user)
            cart_items = CartItem.objects.all().filter(cart=cart[:1])

            for cart_item in cart_items:
                item_count +=  cart_item.quantity
            
        except Cart.DoesNotExist:
            item_count = 0
    
    return dict(item_count=item_count)