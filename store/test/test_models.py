from django.test import TestCase
from store.models import Category, Product

from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='test',slug='test')

    def test_category_model_entry(self):
        data=self.data1
        self.assertTrue(isinstance(data,Category))

    def test_category_model_entry(self):
        data=self.data1
        self.assertEqual(str(data),'test')

class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='test',slug='test')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1,title='test beginners',created_by_id=1,
                                            slug='test-beginners', price='20.00', image='test')
    def test_products_model_entry(self):
        data=self.data1
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data),'test beginners')