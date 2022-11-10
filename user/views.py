from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import UserSerializer, TokenObtainSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TokenObtainView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer
