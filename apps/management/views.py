from django.shortcuts import render
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
        # Return the totality of the artists
        queryset = Artists.objects.all()

        return queryset
    
class EmployeesViewSet(ModelViewSet):
    serializer_class = EmployeesSerializer

    def get_queryset(self):
        # Return the totality of the artists
        queryset = Employees.objects.all()

        return queryset