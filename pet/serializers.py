from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'user', 'birth_date', ]
