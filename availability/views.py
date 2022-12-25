from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Availability
from .serializers import AvailabilitySerializer, AvailabilityCreateSerializer
from user.permissions import IsVetUser



class AvailabilityListAPIView(generics.ListAPIView):
    serializer_class = AvailabilitySerializer

    def get_queryset(self):
        vet_id = self.kwargs.get('pk')
        # TODO agregar verificacion si existe el veterinario
        return Availability.objects.filter(user=vet_id)


class AvailabilityCreateAPIView(generics.CreateAPIView):
    serializer_class = AvailabilityCreateSerializer
    permission_classes = [IsAuthenticated, IsVetUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        Availability.objects.create(
            user=self.request.user,
            day=serializer.validated_data['day'],
            start_time = serializer.validated_data['start_time'],
            end_time = serializer.validated_data['end_time'],
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
