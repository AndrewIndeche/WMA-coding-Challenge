from django.test import TestCase
from .models import Customer,Payment,Verification
from django.contrib.auth.models import User

# Create your tests here.
class Customer(TestCase):
    def setUp(self):
        self.new_user = Customer(name="Andrew", email="kiplani@gmail.com", location="Kenya", mobile_number="1234")
        self.new_user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.customer_test, Customer))

    def test_save_profile(self):
        self.customer_test.save_customer()
        after = Customer.objects.all()
        self.assertTrue(len(after) > 0)


#class Payment(TestCase):
#class Verification(TestCase):
