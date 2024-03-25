from django.test import TestCase
from store.models import Category, Product

class CategoryModelTests(TestCase):
    def test_string_representation(self):
        category = Category(name='Books')
        self.assertEqual(str(category), 'Books')

class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')

    def test_string_representation(self):
        product = Product(
            name='iPhone 12',
            description='Apple iPhone 12',
            price=999.99,
            category=self.category
        )
        self.assertEqual(str(product), 'iPhone 12')