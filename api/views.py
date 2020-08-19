from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import Http404

from .serializers import UserSerializer, StoreSerializer, PurchaseSerializer
from .models import User, Store, Purchase

class PingView(APIView):
    def get(self, request, format=None):
        """
        Return 'pong' if it worked.
        """
        return Response({"status": "pong"})
    
class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class StoreList(APIView):
    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

class PurchaseList(APIView):
    def get(self, request, format=None):
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseDetail(APIView):
    def get_object(self, pk):
        try:
            return Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        purchase = self.get_object(pk)
        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data)