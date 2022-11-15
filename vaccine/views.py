from base.views import BasicPermissionViewSet
from .models import Vaccine
from .serializers import VaccineSerializer


class VaccineViewSet(BasicPermissionViewSet):
    serializer_class = VaccineSerializer

    def get_queryset(self):
        return Vaccine.objects.all()
