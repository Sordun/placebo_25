from django.db import models


# Модель для представления подразделений в организации
class Department(models.Model):
    name = models.CharField(max_length=100)
    parent_department = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # Установить null, если родительское подразделение удалено
        related_name='subdepartments'  # Имя обратной связи для доступа к дочерним подразделениям
    )

    # Метод для строкового представления объекта
    def __str__(self):
        return self.name


# Модель для представления должностей в организации
class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Модель для представления сотрудников
class Employee(models.Model):
    # Имя сотрудника
    name = models.CharField(max_length=100)
    # Связь многие ко многим с должностями (один сотрудник может занимать несколько должностей)
    positions = models.ManyToManyField(Position, related_name='employees')
    # Внешний ключ для связи с подразделением, к которому принадлежит сотрудник
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# Модель для представления прав в системе
class Permission(models.Model):
    # Название права
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Модель для связи сотрудников с правами
class EmployeePermission(models.Model):
    # Внешний ключ для связи с сотрудником
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Внешний ключ для связи с правом
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        # Уникальное ограничение, чтобы одно и то же право не могло быть присвоено одному сотруднику несколько раз
        unique_together = ('employee', 'permission')
