from django.db import models
from products.models import Product, DiscountCode
from customers.models import Customer, Address
from django.utils import timezone


class Order(models.Model):
    customer = models.ForeignKey(Customer,related_name="orders",on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    total_price = models.PositiveIntegerField(default=0)
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE,null=True, blank=True)
    CHOICES = (
        ("P","pending"),
        ("A","accepted"),
        ("R","rejected")
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(choices=CHOICES,max_length=1,default="P")

    def get_total_price(self):
        price = 0
        for item in self.items.all():
            price += (item.count * item.product.get_end_price())

        if self.discount_code:
            discount = self.discount_code.discount
            if discount.type == "C":
                price = price - discount.amount
            elif discount.type == "P":
                if discount.max_amount and (price*discount.amount//100) >= discount.max_amount:
                    price = price - discount.max_amount
                else:
                    price = price - (price*discount.amount//100)
        return price
        




class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name="items")
