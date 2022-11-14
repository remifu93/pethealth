from django.urls import path
from .views import VaccinationCreateAPIView

urlpatterns = [
    path('pet/<pk>/', VaccinationCreateAPIView.as_view(), name='vaccination-create'),
]