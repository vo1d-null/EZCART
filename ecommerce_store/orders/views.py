from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
import stripe
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from django.core.mail import send_mail
from django.template.loader import render_to_string

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if request.method == 'POST':
        try:
            total_amount = sum(item.product.price * item.quantity for item in cart_items)

            # Create a Stripe payment intent
            intent = stripe.PaymentIntent.create(
                amount=int(total_amount * 100),  # Amount in cents
                currency='usd',
                metadata={
                    'user_id': request.user.id,
                }
            )

            # Confirm the payment
            return redirect(reverse('orders:confirm_payment', args=[intent.id]))
        except stripe.error.CardError as e:
            # Handle card error
            messages.error(request, e.error.message)
        except Exception as e:
            # Handle other exceptions
            messages.error(request, 'An error occurred during payment. Please try again.')

    return render(request, 'orders/checkout.html', {'cart_items': cart_items})

def confirm_payment(request, intent_id):
    intent = stripe.PaymentIntent.retrieve(intent_id)
    user_id = intent.metadata.user_id
    user = request.user

    if intent.status == 'succeeded':
        order = Order.objects.create(user=user, paid=True)

        for item in CartItem.objects.filter(cart__user=user):
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Clear the cart
        Cart.objects.filter(user=user).delete()

        # Send order confirmation email
        subject = 'Order Confirmation'
        message = render_to_string('orders/order_confirmation_email.html', {
            'order': order,
            'order_items': order.orderitem_set.all(),
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

        return render(request, 'orders/order_confirmation.html', {'order': order})
    else:
        messages.error(request, 'Payment was not successful. Please try again.')
        return redirect('orders:checkout')