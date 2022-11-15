from base.views import BasicPermissionViewSet
from .models import Specie
from .serializers import SpecieSerializer


class SpecieViewSet(BasicPermissionViewSet):
    serializer_class = SpecieSerializer

    def get_queryset(self):
        return Specie.objects.all()
