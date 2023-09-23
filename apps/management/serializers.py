from .models import Customers, Artists
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