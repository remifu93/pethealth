from rest_framework import viewsets
from .models import Vaccine
from .serializers import VaccineSerializer


class VaccineViewSet(viewsets.ModelViewSet):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.all()
