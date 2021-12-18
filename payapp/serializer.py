from rest_framework import serializers
from .models import Customer,Payment,Verification,Subscription
from cloudinary.models import CloudinaryField
from rave_python import Rave

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id",'fullname', 'created_at', 'email', 'mobile_number','location','status')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id",'name','interval','duration','status')
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id','Authorization','amount','status')

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ("id",'status','amount', 'message','data')
