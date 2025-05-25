from rest_framework import serializers
from .models import User, MedicineSchedule

class MedicineScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineSchedule
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    schedules = MedicineScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
