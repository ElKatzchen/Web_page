from rest_framework import viewsets
from .models import User, MedicineSchedule
from .serializer import UserSerializer, MedicineScheduleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MedicineScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicineSchedule.objects.all()
    serializer_class = MedicineScheduleSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('User')
        medicine_count = MedicineSchedule.objects.filter(User_id=user_id).count()
        if medicine_count >= 6:
            return Response({"Max medicine is 6"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)