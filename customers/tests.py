from django.test import TestCase
from .models import Customer, Address
from django.contrib.auth.models import User


class CustomerTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="testuser1", password="testuser1password")
        self.customer1 = Customer.objects.create(user=self.user1, phone="09120000001")
        self.user2 = User.objects.create(username="testuser2", password="testuser2password")
        self.customer2 = Customer.objects.create(user=self.user2, phone="09120000002")

    def test_user_fields(self):
        customer1 = Customer.objects.get(user__username="testuser1")
        customer2 = Customer.objects.get(user__username="testuser2")
        self.assertEqual(customer1.user, self.user1)
        self.assertEqual(customer2.user, self.user2)

    def test_phone_field(self):
        customer1 = Customer.objects.get(user__username="testuser1")
        customer2 = Customer.objects.get(user__username="testuser2")
        self.assertEqual(customer1.phone, "09120000001")
        self.assertEqual(customer2.phone, "09120000002")



class AddressTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="testuser1", password="testuser1password")
        self.customer1 = Customer.objects.create(user=self.user1, phone="09120000001")
        self.user2 = User.objects.create(username="testuser2", password="testuser2password")
        self.customer2 = Customer.objects.create(user=self.user2, phone="09120000002")
        self.address1 = Address.objects.create(customer=self.customer1, city="city1", province="province1",details="detail1")
        self.address2 = Address.objects.create(customer=self.customer1, city="city2", province="province2",details="detail2")
        self.address3 = Address.objects.create(customer=self.customer2, city="city3", province="province3",details="detail3")
        self.address4 = Address.objects.create(customer=self.customer2, city="city4", province="province4",details="detail4")

    def test_customer_field(self):
        address1 = Address.objects.get(city="city1")
        address2 = Address.objects.get(city="city2")
        address3 = Address.objects.get(city="city3")
        address4 = Address.objects.get(city="city4")

        self.assertEqual(address1.customer, self.customer1)
        self.assertEqual(address1.customer, address2.customer)
        self.assertEqual(address3.customer, self.customer2)
        self.assertEqual(address3.customer, address4.customer)

    def test_city_field(self):
        address1 = Address.objects.get(province="province1")
        address2 = Address.objects.get(province="province2")
        address3 = Address.objects.get(province="province3")
        address4 = Address.objects.get(province="province4")

        self.assertEqual(address1.city, "city1")
        self.assertEqual(address2.city, "city2")
        self.assertEqual(address3.city, "city3")
        self.assertEqual(address4.city, "city4")
    
    def test_province_field(self):
        address1 = Address.objects.get(city="city1")
        address2 = Address.objects.get(city="city2")
        address3 = Address.objects.get(city="city3")
        address4 = Address.objects.get(city="city4")

        self.assertEqual(address1.province, "province1")
        self.assertEqual(address2.province, "province2")
        self.assertEqual(address3.province, "province3")
        self.assertEqual(address4.province, "province4")

    def test_details_field(self):
        address1 = Address.objects.get(city="city1")
        address2 = Address.objects.get(city="city2")
        address3 = Address.objects.get(city="city3")
        address4 = Address.objects.get(city="city4")

        self.assertEqual(address1.details, "detail1")
        self.assertEqual(address2.details, "detail2")
        self.assertEqual(address3.details, "detail3")
        self.assertEqual(address4.details, "detail4")