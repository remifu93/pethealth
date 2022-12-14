from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Pet
from .serializers import PetSerializer, PetDetailSerializer


class PetListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Pet.objects.filter(user=self.request.user.id, active=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Pet.objects.filter(user=self.request.user.id, active=True)

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
