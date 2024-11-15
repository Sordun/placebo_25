from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PositionViewSet, EmployeeViewSet, PermissionViewSet, EmployeePermissionViewSet

router = DefaultRouter()
router.register(r"departments", DepartmentViewSet)
router.register(r"positions", PositionViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"permissions", PermissionViewSet)
router.register(r"employee-permissions", EmployeePermissionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
