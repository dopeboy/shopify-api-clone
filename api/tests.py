from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.http import HttpResponse
from django.urls import reverse
from .models import User, Store, Purchase
from . import views

# Create your tests here.
class TestCases(TestCase):
    def setUp(self):
        User.objects.create(name="John Doe", preferences=["male", "men under 25"])
        User.objects.create(name="Jane Doe", preferences=["female", "women over 30"])

        Store.objects.create(store_name="Store1", category="Clothing", products=["Jacket", "T-Shirt"])
        Store.objects.create(store_name="Store2", category="Household", products=["Paper Towels", "Detergent"])

    def test(self):
        user1 = User.objects.get(name='John Doe')
        user2 = User.objects.get(name='Jane Doe')

        self.assertEqual(user1.preferences, ['male', 'men under 25'])
        self.assertEqual(user2.preferences, ['female', 'women over 30'])

        store1 = Store.objects.get(store_name='Store1')
        store2 = Store.objects.get(store_name='Store2')
        
        self.assertEqual(store1.category, "Clothing")
        self.assertEqual(store1.products, ["Jacket", "T-Shirt"])

        self.assertEqual(store2.category, "Household")
        self.assertEqual(store2.products, ["Paper Towels", "Detergent"])

        Purchase.objects.create(user=user1, store=store1, products=['Jacket'])
        Purchase.objects.create(user=user2, store=store2, products=['Paper Towels'])

        purchase1 = Purchase.objects.get(user=user1)
        purchase2 = Purchase.objects.get(user=user2)

        self.assertEqual(purchase1.user, user1)
        self.assertEqual(purchase2.store, store2)

        factory = APIRequestFactory()

        request1 = factory.get('/users/')
        view1 = views.UserList.as_view()
        response1 = view1(request1)
        assert response1.status_code == 200
        
        request2 = factory.get('/stores/')
        view2 = views.StoreList.as_view()
        response2 = view2(request2)
        assert response2.status_code == 200
    
        request3 = factory.get('/purchases/')
        view3 = views.PurchaseList.as_view()
        response3 = view3(request3)
        assert response3.status_code == 200