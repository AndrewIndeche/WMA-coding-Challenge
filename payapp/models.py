from django.db import models
from rave_python import Rave
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    mobile_number = models.IntegerField(null=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100, help_text="The status of this subscription.")


class Payment(models.Model):
    card_number = models.CharField(max_length=100)
    cvv = models.IntegerField(null=True)
    currency = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    tx_ref = models.CharField(max_length=100)
    account_number = models.IntegerField(null=True)
    account_name = models.CharField(max_length=100)


class Verification(models.Model):
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    data = models.CharField(max_length=300)
