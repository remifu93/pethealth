from rest_framework import serializers
from vaccination.serializers import VaccinationSerializer
from race.serializers import RaceSerializer
from .models import Pet



class PetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'user',
            'birth_date',
            'race',
            'weight',
            'sex',
            'created',
            'modified',
            'active',
        ]


class PetDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    vaccination = serializers.SerializerMethodField()
    race = RaceSerializer()
    sex = serializers.SerializerMethodField()

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

    def get_sex(self, obj):
        return obj.get_sex_display()
