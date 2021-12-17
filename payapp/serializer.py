from rest_framework import serializers
from .models import Customer,Payment,Verification
from cloudinary.models import CloudinaryField
from rave_python import Rave

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('fullname', 'created_at', 'email', 'mobile_number','location','status')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('card_number', 'cvv', 'currency', 'amount ','tx_ref ','account_number','account_name',)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('status', 'message', 'date',)
