from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['province','city','details']

class CustomerSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(source="address_set", many=True, required=False,read_only=True)
    class Meta:
        model = Customer
        fields = ['phone','addresses']

class UserSerializer(serializers.ModelSerializer):
    customer_profile = CustomerSerializer(required=False,read_only=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name' ,'email', 'customer_profile']