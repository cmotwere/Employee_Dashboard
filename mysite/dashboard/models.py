from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    performance_score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
