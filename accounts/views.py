from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomSignUpForm


class SignUpView(CreateView):
    """
    Enhanced signup view with optional admin permissions.
    """

    form_class = CustomSignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """Log the user in after successful signup."""
        response = super().form_valid(form)
        login(self.request, self.object)
        
        # Create appropriate success message based on role selection
        role = form.cleaned_data.get('role')
        if role == 'manager':
            messages.success(
                self.request, 
                f"Manager account created successfully! Welcome, {self.object.username}!"
            )
        elif role == 'supervisor':
            messages.success(
                self.request, 
                f"Supervisor account created successfully! Welcome, {self.object.username}!"
            )
        else:
            messages.success(
                self.request, 
                f"Account created successfully! Welcome, {self.object.username}!"
            )
        return response


class CustomLoginView(LoginView):
    """
    Secure login view with CSRF protection.
    """

    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Add success message on login."""
        messages.success(self.request, f"Welcome back, {form.get_user().username}!")
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    """
    Secure logout view.
    """

    next_page = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        """Add success message on logout."""
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
