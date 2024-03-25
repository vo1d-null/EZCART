from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    actions = ['make_discount']

    def make_discount(self, request, queryset):
        queryset.update(price=F('price') * 0.8)
    make_discount.short_description = "Apply 20% discount"

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)