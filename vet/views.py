from rest_framework import status, generics
from user.models import User
from user.serializers import UserSerializer


class VetListApiView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_vet_user=True)
