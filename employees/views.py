from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .forms import EmployeeForm
from .models import Employee


class EmployeeListView(ListView):
    """Public view: list active employees for presentation."""

    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"

    def get_queryset(self):
        return Employee.objects.filter(is_active=True)


class EmployeeDetailView(DetailView):
    """Public view: show details of a single active employee."""

    model = Employee
    template_name = "employees/employee_detail.html"
    context_object_name = "employee"

    def get_queryset(self):
        return Employee.objects.filter(is_active=True)


class EmployeeAdminListView(LoginRequiredMixin, ListView):
    """
    Admin-only list of all employees, requires login.

    This demonstrates securing views with Django's auth system.
    """

    model = Employee
    template_name = "employees/employee_admin_list.html"
    context_object_name = "employees"
    login_url = "accounts:login"


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    """Admin-only view for creating new employees."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employees:admin_list")
    login_url = "accounts:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Employee"
        return context

    def form_valid(self, form):
        messages.success(self.request, f"Employee '{form.instance.first_name} {form.instance.last_name}' has been added successfully!")
        return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    """Admin-only view for editing existing employees."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employees:admin_list")
    login_url = "accounts:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Employee"
        return context

    def form_valid(self, form):
        messages.success(self.request, f"Employee '{form.instance.first_name} {form.instance.last_name}' has been updated successfully!")
        return super().form_valid(form)


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    """Admin-only view for deleting employees."""

    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("employees:admin_list")
    login_url = "accounts:login"

    def delete(self, request, *args, **kwargs):
        employee = self.get_object()
        messages.success(self.request, f"Employee '{employee.first_name} {employee.last_name}' has been deleted successfully!")
        return super().delete(request, *args, **kwargs)

