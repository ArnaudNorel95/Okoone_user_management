from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import *

class CustomersViewSet(ReadOnlyModelViewSet):
    serializer_class = CustomersSerializer

    def get_queryset(self):
        # Return the totality of the customers
        queryset = Customers.objects.all()

        return queryset
    
class ArtistsViewSet(ModelViewSet):
    serializer_class = ArtistsSerializer

    def get_queryset(self):
        # Return the totality of the customers
        queryset = Artists.objects.all()

        return queryset