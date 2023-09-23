from .models import Customers, Artists, Employees
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import ValidationError

class CustomersSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"

class ArtistsSerializer(ModelSerializer):
    class Meta:
        model = Artists
        fields = "__all__"

class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"