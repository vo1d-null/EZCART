from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from cart.models import Cart, CartItem

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.delete()
        return redirect('orders:order_confirmation', order.id)
    return render(request, 'orders/checkout.html', {'cart_items': cart_items})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'orders/order_confirmation.html', {'order': order, 'order_items': order_items})