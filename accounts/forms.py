from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomSignUpForm(UserCreationForm):
    """Enhanced signup form with role-based admin permissions."""
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )
    
    ROLE_CHOICES = [
        ('', '--- Select Role ---'),
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        help_text="Select an admin role if this user needs management access."
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 
            'password1', 'password2', 'role'
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a secure password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'role':
                field.widget.attrs['class'] = 'form-control'
        
        # Add help text for username field
        self.fields['username'].help_text = (
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        )
        
        # Add help text for password fields
        self.fields['password1'].help_text = (
            "Your password can't be too similar to your other personal information, "
            "must contain at least 8 characters, can't be a commonly used password, "
            "and can't be entirely numeric."
        )
        self.fields['password2'].help_text = "Enter the same password as before, for verification."

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        # Set staff status based on role selection
        role = self.cleaned_data.get('role')
        user.is_staff = bool(role)  # Staff if any role is selected
        user.is_superuser = False  # Never create superusers through signup
        
        if commit:
            user.save()
            # Store role in user profile or session if needed for future reference
            # For now, we'll use the staff status to determine admin access
        return user
