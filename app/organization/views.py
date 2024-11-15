from rest_framework import viewsets
from .models import Department, Position, Employee, Permission, EmployeePermission
from .serializers import (
    DepartmentSerializer,
    PositionSerializer,
    EmployeeSerializer,
    PermissionSerializer,
    EmployeePermissionSerializer
)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class EmployeePermissionViewSet(viewsets.ModelViewSet):
    queryset = EmployeePermission.objects.all()
    serializer_class = EmployeePermissionSerializer
