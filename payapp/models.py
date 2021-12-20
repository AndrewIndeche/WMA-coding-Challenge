from django.db import models
from rave_python import Rave
from django.contrib.auth.models import User
from django.urls import reverse
from url_or_relative_url_field.fields import URLOrRelativeURLField

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    mobile_number = models.IntegerField(blank=True)
    location = models.CharField(max_length=100)

class Payment(models.Model):
    PREMIUM = 'is_premium'
    NOTPREMIUM ='is_not_premium'

    duration = models.IntegerField(blank=True)
    interval = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(blank=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    data = models.CharField(max_length=300)

    def __str__(self):
        return self.status
