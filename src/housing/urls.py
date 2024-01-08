from rest_framework.routers import DefaultRouter
from housing.views import ApartmentViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'apartments', ApartmentViewSet)
router.register(r'reservations', ReservationViewSet)