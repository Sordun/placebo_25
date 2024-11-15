from django.contrib import admin

from .models import Employee, EmployeePermission, Department, Position, Permission

admin.site.register(Employee)
admin.site.register(EmployeePermission)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Permission)
