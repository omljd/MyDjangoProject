from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """Form for creating and editing Employee instances."""

    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name", 
            "job_title",
            "department",
            "email",
            "phone_number",
            "photo",
            "bio",
            "is_active",
        ]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
