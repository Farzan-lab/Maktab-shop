from django.test import TestCase
from .models import Discount, Category, Product, DiscountCode


class DiscountTestCase(TestCase):
    def setUp(self):
        self.discount1 = Discount.objects.create(type="C",amount=1000)
        self.discount2 = Discount.objects.create(type="P",amount=10,max_amount=1000)
    
    def test_type_field(self):
        discount1 = Discount.objects.get(id=self.discount1.id)
        discount2 = Discount.objects.get(id=self.discount2.id)
        self.assertEqual(discount1.type,"C")
        self.assertEqual(discount2.type,"P")

    def test_amount_field(self):
        discount1 = Discount.objects.get(id=self.discount1.id)
        discount2 = Discount.objects.get(id=self.discount2.id)
        self.assertEqual(discount1.amount,1000)
        self.assertEqual(discount2.amount,10)
    
    def test_max_amount_field(self):
        discount1 = Discount.objects.get(id=self.discount1.id)
        discount2 = Discount.objects.get(id=self.discount2.id)
        self.assertEqual(discount1.max_amount,None)
        self.assertEqual(discount2.max_amount,1000)


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="parent_category")
        self.category2 = Category.objects.create(name="child1_category",parent=self.category1)
        self.category3 = Category.objects.create(name="child2_category",parent=self.category1)
        self.category4 = Category.objects.create(name="grand_child1_category",parent=self.category2)

    def test_get_parents_method(self):
        grand_child = Category.objects.get(id=self.category4.id)
        parents = grand_child.get_parents()
        actuall_parents = [self.category1, self.category2, self.category4]
        self.assertEqual(parents, actuall_parents)

    def test_get_children_method(self):
        parent = Category.objects.get(id=self.category1.id)
        children = parent.get_children()
        actuall_children = [self.category2,self.category3, self.category1]
        self.assertEqual(children, actuall_children)

    def test_name_field(self):
        category1 = Category.objects.get(id=self.category1.id)
        category2 = Category.objects.get(id=self.category2.id)
        category3 = Category.objects.get(id=self.category3.id)
        category4 = Category.objects.get(id=self.category4.id)

        self.assertEqual(category1.name, "parent_category")
        self.assertEqual(category2.name, "child1_category")
        self.assertEqual(category3.name, "child2_category")
        self.assertEqual(category4.name, "grand_child1_category")


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="some_category")
        self.discount1 = Discount.objects.create(type="C",amount=10)
        self.product1 = Product.objects.create(title="product1",description="description1",brand="brand1",available=10,image="image1",price=1000,discount=self.discount1, category=self.category )

    def test_get_price_method(self):
        product = Product.objects.get(id=self.product1.id)
        self.assertEqual(product.get_end_price(),990)

    def test_title_field(self):
        product = Product.objects.get(id=self.product1.id)
        self.assertEqual(product.title,"product1")

class DiscountCodeTestCase(TestCase):
    def setUp(self):
        self.discount1 = Discount.objects.create(type="C",amount=10)
        self.discount_code = DiscountCode.objects.create(code="d-123456",discount=self.discount1)

    def test_code_field(self):
        discount_code = DiscountCode.objects.get(id=self.discount_code.id)
        self.assertEqual(discount_code.code, "d-123456")

    def test_discount_field(self):
        discount_code = DiscountCode.objects.get(id=self.discount_code.id)
        self.assertEqual(discount_code.discount, self.discount1)
    
    
