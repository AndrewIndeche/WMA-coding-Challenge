
from django.shortcuts import render
from django.db.models.query import QuerySet
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
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny, IsAuthenticated


# rest api ====================================

class CustomerViews(APIView):
    """
    Edit and get Customer details
    """
    def post(self,request,format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PaymentView(APIView):
    """
    View and make payments
    """
    def get(self,request,format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "is_premium", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "is_premium", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionView(APIView):
    """
    View subscriptions status
    """

    def get(self, request,pk):
        subscription = self.get(pk)
        serializers = SubscriptionSerializer(subscritpion,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # delete employee
        notes = self.get(pk)
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VerificationView(APIView):
    """
    View status and message on verification
    """

    def get(self, request,pk):
        verification = self.get(pk)
        serializers = VerificationSerializer(verification,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
