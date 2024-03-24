from django.shortcuts import render
from django.db.models import Q
from store.models import Product

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )
    return render(request, 'search/search_results.html', {'products': products, 'query': query})