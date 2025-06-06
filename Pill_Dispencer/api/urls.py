from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MedicineScheduleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'medicine', MedicineScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
