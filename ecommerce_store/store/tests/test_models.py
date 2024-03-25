from django.test import TestCase
from store.models import Category, Product

class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Books')

    def test_product_creation(self):
        product = Product.objects.create(
            name='Python Book',
            description='Learn Python programming',
            price=29.99,
            category=self.category
        )
        self.assertIsInstance(product, Product)
        self.assertEqual(str(product), 'Python Book')

    def test_product_price(self):
        product = Product.objects.create(
            name='JavaScript Book',
            description='Learn JavaScript',
            price=19.99,
            category=self.category
        )
        self.assertEqual(product.price, 19.99)