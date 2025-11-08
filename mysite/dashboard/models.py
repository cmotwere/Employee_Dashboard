from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    ROLE_CHOICES = [
        ('HR', 'Human Resources'),
        ('EMP', 'Employee'),
        ('MGR', 'Manager'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    performance_score = models.IntegerField()
    date = models.DateField()  # Keep this for performance review date
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='EMP')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Employees"