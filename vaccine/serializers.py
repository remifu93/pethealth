from rest_framework import serializers
from .models import Vaccine, Vaccination


class VaccineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vaccine
        fields = ['id', 'name', ]


class VaccinationSerializer(serializers.ModelSerializer):
    vaccine = VaccineSerializer()

    class Meta:
        model = Vaccination
        fields = ['id', 'vaccine', 'date_placed', 'created', 'modified', ]
