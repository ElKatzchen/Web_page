from rest_framework import viewsets
from .models import User, MedicineSchedule
from .serializer import UserSerializer, MedicineScheduleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MedicineScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicineSchedule.objects.all()
    serializer_class = MedicineScheduleSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('User')
        medicine_count = MedicineSchedule.objects.filter(User_id=user_id).filter(MedicineName=request.data.get('MedicineName')).count()
        if medicine_count >= 6:
            return Response({"Max medicine is 6"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='delete_medicine')
    def delete_medicine(self, request, *args, **kwargs):
        user_id = request.data.get('User') or request.query_params.get('User')
        med_id = request.data.get('id') or request.query_params.get('id')
        if not user_id or not med_id:
            return Response({"detail": "User and id are required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            med_schedule = MedicineSchedule.objects.get(pk=med_id, User_id=user_id)
        except MedicineSchedule.DoesNotExist:
            return Response({"detail": "Medicine not found for this user."}, status=status.HTTP_404_NOT_FOUND)
        med_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)