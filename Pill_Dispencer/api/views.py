from rest_framework import viewsets
from .models import User, MedicineSchedule
from .serializer import UserSerializer, MedicineScheduleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MedicineScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicineSchedule.objects.all()
    serializer_class = MedicineScheduleSerializer