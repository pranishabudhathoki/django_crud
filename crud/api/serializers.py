from pyexpat import model
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model = Employee
