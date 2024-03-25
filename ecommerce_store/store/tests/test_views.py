from django.test import TestCase, Client
from django.urls import reverse
from store.models import Category, Product

class ProductListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Books')
        self.product = Product.objects.create(
            name='Python Book',
            description='Learn Python programming',
            price=29.99,
            category=self.category
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('store:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Book')

    def test_product_list_view_filtered_by_category(self):
        response = self.client.get(reverse('store:product_list') + '?category=' + str(self.category.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Book')

class ProductDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Books')
        self.product = Product.objects.create(
            name='Python Book',
            description='Learn Python programming',
            price=29.99,
            category=self.category
        )

    def test_product_detail_view(self):
        response = self.client.get(reverse('store:product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Book')