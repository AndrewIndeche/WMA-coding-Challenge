from django.db import models
from rave_python import Rave
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    mobile_number = models.IntegerField(null=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Payment(models.Model):
    PREMIUM = 'is_premium'
    NOTPREMIUM ='is_not_premium'

    id = models.AutoField(primary_key=True)
    duration = models.IntegerField(null=True)
    interval = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(null=True)
    PAYMENT_STATUS = (
        (PREMIUM, 'is_premium'),
        (NOTPREMIUM, 'is_not_premium'),
    )
    status = models.CharField(max_length=100, choices=PAYMENT_STATUS,default='is_not_premium', help_text="The status of this subscription.")

    def __str__(self):
        return self.status

class Subscription(models.Model):
    id = models.IntegerField (primary_key=True)
    Authorization = models.CharField(max_length=100)

    def __str__(self):
        return self.Authorization

class Verification(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    data = models.CharField(max_length=300)

    def __str__(self):
        return self.status
