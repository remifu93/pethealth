from base.views import BasicPermissionViewSet
from .models import Race
from .serializers import RaceSerializer


class RaceViewSet(BasicPermissionViewSet):
    serializer_class = RaceSerializer

    def get_queryset(self):
        queryset = Race.objects.all()
        specie = self.request.query_params.get('specie')
        if specie is not None:
            queryset = queryset.filter(specie_id=specie)
        return queryset

