from django.test import TestCase
from .models import Order,OrderItem
from customers.models import Customer,Address
from products.models import Product,Category
from django.contrib.auth.models import User


class OrderTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="testuser1",password="testuser1password")
        self.customer1 = Customer.objects.create(user=self.user1,phone="09120000001")

        self.address1 = Address.objects.create(customer=self.customer1,city="city1",province="province1",details="detail1")
        self.order = Order.objects.create(customer=self.customer1,address=self.address1,status="P")
        self.category1 = Category.objects.create(name="category1")
        self.product1 = Product.objects.create(title="product1",description="description1",brand="brand1",available=10,image="image1",price=1000, category=self.category1 )
        self.product2 = Product.objects.create(title="product2",description="description2",brand="brand2",available=10,image="image2",price=5000, category=self.category1 )

        self.order_item1 = OrderItem.objects.create(product=self.product1,count=5,order=self.order)
        self.order_item2 = OrderItem.objects.create(product=self.product2,count=2,order=self.order)


    def test_get_total_price_method(self):
        self.assertEqual(self.order.get_total_price(),15000)

    def test_customer_field(self):
        order = Order.objects.get(id=self.customer1.id)
        self.assertEqual(order.customer,self.customer1)


class OrderItemTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="testuser1",password="testuser1password")
        self.customer1 = Customer.objects.create(user=self.user1,phone="09120000001")

        self.address1 = Address.objects.create(customer=self.customer1,city="city1",province="province1",details="detail1")
        self.order = Order.objects.create(customer=self.customer1,address=self.address1,status="P")
        self.category1 = Category.objects.create(name="category1")
        self.product1 = Product.objects.create(title="product1",description="description1",brand="brand1",available=10,image="image1",price=1000, category=self.category1 )

        self.order_item1 = OrderItem.objects.create(product=self.product1,count=5,order=self.order)

    def test_product_field(self):
        order_item = OrderItem.objects.get(id=self.order_item1.id)
        self.assertEqual(order_item.product,self.product1)

    def test_count_field(self):
        order_item = OrderItem.objects.get(id=self.order_item1.id)
        self.assertEqual(order_item.count,5)
    
    def test_order_field(self):
        order_item = OrderItem.objects.get(id=self.order_item1.id)
        self.assertEqual(order_item.order,self.order)