from .models import Customers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import ValidationError

class CustomersSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = ["id", "first_name", "last_name", "company"]
