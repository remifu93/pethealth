from rest_framework import serializers
from vaccine.serializers import VaccineSerializer
from .models import Vaccination


class VaccinationSerializer(serializers.ModelSerializer):
    vaccine = VaccineSerializer(read_only=True)

    class Meta:
        model = Vaccination
        fields = ['id', 'vaccine', 'date_placed', 'created', 'modified', ]


class VaccinationCreateSerializer(serializers.Serializer):
    vaccine = serializers.IntegerField()
    date_placed = serializers.DateField()

