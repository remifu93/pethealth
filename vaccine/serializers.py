from rest_framework import serializers
from .models import Vaccine, Vaccination


class VaccineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vaccine
        fields = ['id', 'name', ]


class VaccinationSerializer(serializers.ModelSerializer):
    vaccine = VaccineSerializer(read_only=True)

    class Meta:
        model = Vaccination
        fields = ['id', 'vaccine', 'date_placed', 'created', 'modified', ]


class VaccinationCreateSerializer(serializers.Serializer):
    vaccine = serializers.IntegerField()
    date_placed = serializers.DateField()
