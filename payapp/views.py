from django.shortcuts import render
import requests
from django.contrib.auth.models import User
from .models import Customer,Payment
from .serializer import CustomerSerializer,CustomerCreateSerializer,PaymentSerializer

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
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = CustomerSerializer(users, many=True)
        return Response(serializer.data)



class PaymentView(APIView):
    """
    List all users.
    """
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = PaymentSerializer(users, many=True)
        return Response(serializer.data)

class VerificationView(APIView):
    """
    List all users.
    """
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = PaymentSerializer(users, many=True)
        return Response(serializer.data)
