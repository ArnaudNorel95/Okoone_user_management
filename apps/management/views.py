from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from .user_management import get_customers
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import *

# Create your views here.
class CustomersViewSet(ReadOnlyModelViewSet):

    serializer_class = CustomersSerializer
    # detail_serializer_class = CustomerDetailSerializer

    def get_queryset(self):
        # Return the totality of the customers not in detail
        queryset = Customers.objects.all()

        return queryset