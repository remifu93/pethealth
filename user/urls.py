from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserCreateAPIView, TokenObtainView


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('login/', TokenObtainView.as_view(), name='user-login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='user-refresh'),
]
