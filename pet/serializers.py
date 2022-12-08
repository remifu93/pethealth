from rest_framework import serializers
from vaccination.serializers import VaccinationSerializer
from .models import Pet



class PetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'user', 'birth_date', 'created', 'modified', 'active', ]


class PetDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    vaccination = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'user',
            'birth_date',
            'race',
            'sex',
            'weight',
            'vaccination',
            'created',
            'modified',
            'active',
        ]

    def get_vaccination(self, obj):
        queryset = obj.vaccination_set.all()
        return VaccinationSerializer(queryset, many=True).data
