from rest_framework import serializers
from specie.serializers import SpecieSerializer
from .models import Race


class RaceSerializer(serializers.ModelSerializer):
    specie = SpecieSerializer(read_only=True)

    class Meta:
        model = Race
        fields = ['id', 'name', 'specie', ]
