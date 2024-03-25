from django.views.generic import ListView, DetailView
from django.db.models import Count, Q
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    paginate_by = 12
    ordering = ['-id']  # Order by newest products first

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        query = self.request.GET.get('q')
        price_range = self.request.GET.get('price_range')

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        if price_range:
            min_price, max_price = price_range.split('-')
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.annotate(product_count=Count('product'))
        price_ranges = [
            ('0-100', 'Under $100'),
            ('100-500', '$100 - $500'),
            ('500-1000', '$500 - $1000'),
            ('1000-', 'Over $1000'),
        ]
        context['categories'] = categories
        context['price_ranges'] = price_ranges
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
