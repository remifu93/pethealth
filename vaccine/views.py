from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Vaccine
from .serializers import VaccineSerializer


class VaccineViewSet(viewsets.ModelViewSet):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
