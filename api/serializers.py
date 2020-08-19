from rest_framework import serializers
from .models import User, Store, Purchase

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'preferences')

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('store_name', 'category', 'products')

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False)
    store = serializers.StringRelatedField(many=False)
    class Meta:
        model = Purchase
        fields = ('user', 'store', 'products')
