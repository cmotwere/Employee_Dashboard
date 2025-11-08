from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseForbidden
from dashboard.models import Employee
from .forms import EmployeeForm, PerformanceForm

@login_required
def employee_dashboard(request):
    try:
        employee = Employee.objects.get(user=request.user)
        is_hr = employee.role == 'HR'
        
        if is_hr:
            employees = Employee.objects.all()
        else:
            employees = Employee.objects.filter(user=request.user)
            
        return render(request, 'user_management/dashboard.html', {
            'employees': employees,
            'is_hr': is_hr,
            'current_employee': employee
        })
    except Employee.DoesNotExist:
        messages.error(request, "Employee profile not found.")
        return redirect('user_management:login')

@login_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    current_employee = Employee.objects.get(user=request.user)
    
    if current_employee.role != 'HR' and employee.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this employee.")
    
    if request.method == 'POST':
        if current_employee.role == 'HR':
            form = EmployeeForm(request.POST, instance=employee)
        else:
            form = PerformanceForm(request.POST, instance=employee)
            
        if form.is_valid():
            form.save()
            messages.success(request, "Employee data updated successfully!")
            return redirect('user_management:employee_dashboard')
    else:
        if current_employee.role == 'HR':
            form = EmployeeForm(instance=employee)
        else:
            form = PerformanceForm(instance=employee)
    
    return render(request, 'user_management/edit_employee.html', {
        'form': form,
        'employee': employee,
        'is_hr': current_employee.role == 'HR'
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('user_management:employee_dashboard')  # Fixed: redirect to dashboard
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'user_management/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_management:login')