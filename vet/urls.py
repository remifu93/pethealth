from django.urls import path
from .views import VetListApiView

urlpatterns = [
    path('list/', VetListApiView.as_view(), name='vet-list'),
]