from django.urls import path
from company_employee.views import CompanyEmployeeData

urlpatterns = [
    path('', CompanyEmployeeData.as_view(), name='company_employee_data')
]
