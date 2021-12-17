from django.shortcuts import render
import requests
from django.contrib.auth.models import User
from .models import Customer,Payment,Verification
from .serializer import CustomerSerializer,PaymentSerializer,VerificationSerializer

# api.
from django.http import JsonResponse
from rest_framework import status,generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rave_python import Rave

# rest api ====================================

class CustomerView(APIView):
    """
    View Customer details.
    """
    def get(self, request):
        #customer = Customer.objects.all().values {'fullname', 'created_at', 'email', 'mobile_number','location','status'}
        response = requests.get ('https://api.flutterwave.com/v3/charges?type=card').json()
        return JsonResponse(customer.data)

class PaymentView(APIView):
    """
    View specifics of a payment.
    """

    def post(self, request):
        #payment = Payment.objects.all().values {'card_number', 'cvv ', 'currency', 'amount','tx_ref ','account_number','account_name'}
        response = requests.post ('https://api.flutterwave.com/v3/charges?type=mpesa').json()
        return JsonResponse(payment.data)

class VerificationView(APIView):
    """
    View status and message on verification
    """

    def get(self, request):
        #verification = Verification.objects.all().values {'status', 'message','data'}
        response = requests.get ('https://api.flutterwave.com/v3/transactions/123456/verify').json()
        return JsonResponse(Verification.data)
