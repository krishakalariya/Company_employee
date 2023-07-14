import pandas as pd
from rest_framework import generics
from rest_framework.response import Response

from django_basic.company_employee.constants import COMPANY_EMPLOYEE_CREATED
from django_basic.company_employee.models import Company, Employee
from django_basic.company_employee.serializers import CompanySerializer, EmployeeSerializer, CompanyEmployeeSerializer


class CompanyEmployeeData(generics.ListCreateAPIView):
    serializer_class = CompanyEmployeeSerializer
    queryset = Company.objects.prefetch_related('company_employees')

    def post(self, request):
        Company.objects.all().delete()

        data = pd.read_excel('company_employee/DataFiles/Practical Task Python Sheet.xlsx')
        data = data.groupby('COMPANY_NAME')
        companies = []
        employees = []

        for company_name, employee_data in data:

            company_serializer = CompanySerializer(data={'name': company_name})
            company_serializer.is_valid(raise_exception=True)

            # Create the company instance
            company = Company(**company_serializer.validated_data)
            companies.append(company)

            # Create employee instances for the company
            employee_data = employee_data.to_dict(orient='records')
            for employee_data in employee_data:
                employee_serializer = EmployeeSerializer(
                    data={'first_name': employee_data.get('FIRST_NAME'), 'last_name': employee_data.get('LAST_NAME'),
                          'phone_number': employee_data.get('PHONE_NUMBER').replace('.', ''),
                          'salary': employee_data.get('SALARY')})
                employee_serializer.is_valid(raise_exception=True)
                employees.append(Employee(**employee_serializer.validated_data, company=company))

        # Bulk create the companies and employees
        Company.objects.bulk_create(companies)
        Employee.objects.bulk_create(employees)

        return Response(COMPANY_EMPLOYEE_CREATED, status=201)



