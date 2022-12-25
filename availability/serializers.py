from rest_framework import serializers
from .models import Availability


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = ['id', 'user', 'day', 'start_time', 'end_time', ]


class AvailabilityCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = ['id', 'day', 'start_time', 'end_time', ]
