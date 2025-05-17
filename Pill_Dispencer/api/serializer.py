from rest_framework import serializers
from .models import User, MedicineSchedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MedicineScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineSchedule
        fields = '__all__'