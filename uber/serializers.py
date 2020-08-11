from rest_framework import serializers
from .models import Cab, Rider


class CabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = "__all__"


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'

