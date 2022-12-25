from django.urls import path
from .views import AvailabilityListAPIView, AvailabilityCreateAPIView

urlpatterns = [
    path('vet/<int:pk>/', AvailabilityListAPIView.as_view(), name='availability-list'),
    path('create/', AvailabilityCreateAPIView.as_view(), name='availability-create'),
]