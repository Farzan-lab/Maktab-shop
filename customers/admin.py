from django.contrib import admin
from .models import Customer, Address


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
admin.site.register(Customer, CustomerAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'province','get_username')

    def get_username(self,obj):
        return obj.customer.user
admin.site.register(Address, AddressAdmin)