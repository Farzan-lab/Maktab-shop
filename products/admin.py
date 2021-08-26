from django.contrib import admin
from .models import Discount, DiscountCode, Category, Product

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount', 'max_amount')
admin.site.register(Discount,DiscountAdmin)

class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
admin.site.register(DiscountCode,DiscountCodeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'available', 'price', 'discount')
admin.site.register(Product, ProductAdmin)