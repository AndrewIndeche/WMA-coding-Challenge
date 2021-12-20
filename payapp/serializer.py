from rest_framework import fields, serializers, validators
from .models import Customer,Payment,Subscription,Verification
from django.db.models import fields

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fullname','created_at','mobile_number','location']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('name','amount','interval','duration')
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('__all__')

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('__all__')
