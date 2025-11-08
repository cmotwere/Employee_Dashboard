from django import forms
from dashboard.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'performance_score', 'date', 'role']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'performance_score': forms.NumberInput(attrs={'min': 0, 'max': 100})
        }

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['performance_score']
        widgets = {
            'performance_score': forms.NumberInput(attrs={'min': 0, 'max': 100})
        }