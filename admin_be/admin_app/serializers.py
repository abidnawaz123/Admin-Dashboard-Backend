from .models import *
from rest_framework import serializers

class LatestCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestCustomers
        fields = '__all__'