from rest_framework import serializers
from company_employee.models import Employee, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'salary']


class CompanyEmployeeSerializer(serializers.ModelSerializer):
    company_employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'company_employees']
