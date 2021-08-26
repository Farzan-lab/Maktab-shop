from django.shortcuts import render, redirect
from products.models import Product, DiscountCode
from customers.models import Address
from .models import Order, OrderItem
from django.core.exceptions import PermissionDenied, ValidationError, ObjectDoesNotExist
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    if request.method == "POST":
        try:
            request.user.customer_profile
            try:
                discount = DiscountCode.objects.get(code=request.POST.get('discount'))
            except:
                discount = None

            address = Address(customer=request.user.customer_profile,city=request.POST.get('city'),province=request.POST.get('province'),details=request.POST.get('detail'))
            address.full_clean()
            address.save()
            order = Order(
                customer=request.user.customer_profile,
                discount_code= discount,
                address=address,
            )
            order_items = []
            product_ids = [int(key) for key ,value in request.POST.items() if key.isdecimal()]
            product_objects = Product.objects.filter(id__in=product_ids)
            products_to_update = []
            for product in product_objects:
                if product.available >= int(request.POST.get(f'{product.id}')):
                    product.available = product.available - int(request.POST.get(f'{product.id}'))
                    item = OrderItem(product=product,count=request.POST.get(f'{product.id}'),order=order)
                    order_items.append(item)
                    products_to_update.append(product)
                else:
                    raise ValidationError(('item is not available this much!'))

            order.full_clean()
            order.save()
            OrderItem.objects.bulk_create(order_items)
            Product.objects.bulk_update(products_to_update,fields=['available'])
            order.total_price = order.get_total_price()
            order.save()
            messages.success(request, 'your order is submited successfuly!')
        except Exception as e:
            messages.error(request, "couldnt place your order please fill all the fields!")

    return redirect('home-page')


