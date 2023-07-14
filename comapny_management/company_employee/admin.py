from django.contrib import admin
from django_basic.company_employee.models import Company, Employee

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)