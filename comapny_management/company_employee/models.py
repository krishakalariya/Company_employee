from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Company"
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_employees')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
