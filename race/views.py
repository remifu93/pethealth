from base.views import BasicPermissionViewSet
from .models import Race
from .serializers import RaceSerializer


class RaceViewSet(BasicPermissionViewSet):
    serializer_class = RaceSerializer

    def get_queryset(self):
        return Race.objects.all()
