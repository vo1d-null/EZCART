from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirm_payment/<str:intent_id>/', views.confirm_payment, name='confirm_payment'),  # Use existing view
]
