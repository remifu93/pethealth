from rest_framework.routers import DefaultRouter
from .views import SpecieViewSet

router = DefaultRouter()
router.register('', SpecieViewSet, basename='specie')
urlpatterns = router.urls