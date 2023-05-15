from .models import Location
from rest_framework import serializers
from django.db import models

class LocationSerializer(serializers.Serializer):
    
    lat = serializers.DecimalField(max_digits=22, decimal_places=16)
    long = serializers.DecimalField(max_digits=22, decimal_places=16)