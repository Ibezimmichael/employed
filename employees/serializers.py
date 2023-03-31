from rest_framework import serializers
from employees.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['title']

class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    department = serializers.SlugRelatedField(slug_field='slug', queryset=Department.objects.all())
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone_number', 'created_at', 'department']
        read_only_fields = ['created_at']



