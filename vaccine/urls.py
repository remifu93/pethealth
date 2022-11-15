from rest_framework.routers import DefaultRouter
from .views import VaccineViewSet

router = DefaultRouter()
router.register('', VaccineViewSet, basename='vaccine')
urlpatterns = router.urls