from rest_framework import serializers
from .models import Department, Position, Employee, Permission, EmployeePermission


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class EmployeePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePermission
        fields = '__all__'
