from rest_framework import serializers
from housing.models import *

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Apartment

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Reservation
