from django.db import models



class Discount(models.Model):
    CHOICES = (
        ('C', 'cash'),
        ('P', 'percentage'),
    )
    type = models.CharField(max_length=1,choices=CHOICES)
    amount = models.IntegerField(default=0)
    max_amount = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.amount}-{self.type}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self',null=True , blank=True , on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return f'{self.name}'

    def get_parents(self):
        result = []
        if self.parent:
            result = self.parent.get_parents()
        result.append(self)
        return result   # list of parents

    def get_children(self):
        result = []
        if self.children.exists():
            for child in self.children.all():
                result.append(child)
        result.append(self)
        return result   # list of children

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.CharField(max_length=200)
    available = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="products_picture")
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_end_price(self):
        discount = self.discount
        price = self.price

        if discount:
            if discount.type == "C":
                price = price - discount.amount
            elif discount.type == "P":
                if discount.max_amount and (price*discount.amount//100) >= discount.max_amount:
                    price = price - discount.max_amount
                else:
                    price = price - (price*discount.amount//100)
                    
        return price
                    
            


class DiscountCode(models.Model):
    code = models.CharField(max_length=15)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)


