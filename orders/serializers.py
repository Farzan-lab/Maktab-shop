from rest_framework import serializers
from .models import OrderItem, Order
from products.serializers import ProductSerializer
from customers.serializers import UserSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False, read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product','count']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=False, read_only=True)
    customer = UserSerializer(source="customer.user",required=False,read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
