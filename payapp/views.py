from django.shortcuts import render
import requests
from django.contrib.auth.models import User
from .models import Customer,Payment,Subscription,Verification
from .serializer import CustomerSerializer,PaymentSerializer,SubscriptionSerializer,VerificationSerializer

# api.
from django.http import JsonResponse
from rest_framework import status,generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rave_python import Rave

# rest api ====================================

class CustomerView(APIView):
    def get(self, request,pk):
        customer = self.get(pk)
        serializers = CustomerSerializer(customer,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        customer = self.get(pk)
        serializers = PaymentSerializer(payment,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentView(APIView):
    """
    View specifics of a payment.
    """
    def put(self, request,pk):
        payment = self.get(pk)
        serializers = PaymentSerializer(payment,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionView(APIView):
    """
    View specifics of a payment.
    """

    def get(self, request,pk):
        subscription = self.get(pk)
        serializers = SubscriptionSerializer(subscritpion,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # delete employee
        notes = self.get(pk)
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VerificationView(APIView):
    """
    View status and message on verification
    """

    def get(self, request):
        verification = self.get(pk)
        serializers = VerificationSerializer(verification,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
