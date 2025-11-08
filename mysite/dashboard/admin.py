from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'performance_score', 'date']
    list_filter = ['department', 'date']
    search_fields = ['name', 'department']
    ordering = ['name']