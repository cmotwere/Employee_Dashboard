from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
]