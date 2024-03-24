from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('shipping-policy/', views.shipping_policy, name='shipping_policy'),
    path('faq/', views.faq, name='faq'),
]