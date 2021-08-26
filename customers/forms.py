from django import forms
from django.apps import apps
from django.contrib.auth.models import User
Customer = apps.get_model('customers', 'Customer')
Address = apps.get_model('customers', 'Address')


class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city','province','details']


class CustomerCreationForm(forms.ModelForm):
    phone = forms.CharField(max_length=11)
    class Meta:
        model = Customer
        fields = ['phone']
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name']

class CustomerUpdateForm(forms.ModelForm):
    phone = forms.CharField(max_length=11)
    class Meta:
        model = Customer
        fields = ['phone']