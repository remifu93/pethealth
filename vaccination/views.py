from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from pet.models import Pet
from .serializers import VaccinationCreateSerializer
from .models import Vaccine, Vaccination


class VaccinationCreateAPIView(generics.CreateAPIView):
    serializer_class = VaccinationCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Vaccination.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        pet = get_object_or_404(
            Pet,
            id=self.kwargs.get('pk')
        )

        vaccine = get_object_or_404(
            Vaccine,
            id=serializer.validated_data['vaccine']
        )

        Vaccination.objects.create(
            pet=pet,
            vaccine=vaccine,
            date_placed=serializer.validated_data['date_placed']
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
