from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collections import Counter
from .models import Employee

@login_required
def dashboard_view(request):
    department = request.GET.get('department')
    if department:
        employees = Employee.objects.filter(department=department)
    else:
        employees = Employee.objects.all()

    departments = Employee.objects.values_list('department', flat=True).distinct()
    dept_counts = Counter(employees.values_list('department', flat=True))

    # Debug prints
    print(f"Total employees: {employees.count()}")
    print(f"Departments: {list(departments)}")
    print(f"Dept counts: {dict(dept_counts)}")

    return render(request, 'dashboard/dashboard.html', {
        'employees': employees,
        'departments': departments,
        'selected_department': department,
        'dept_counts': dict(dept_counts)
    })